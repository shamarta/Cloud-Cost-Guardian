import csv
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class CostRecord:
    usage_date: date
    service: str
    cost_usd: Decimal


def read_cost_records(file_path: Path) -> list[CostRecord]:
    records: list[CostRecord] = []
    required_columns = {"date", "service", "cost_usd"}

    with file_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None or not required_columns.issubset(reader.fieldnames):
            raise ValueError("CSV must include date, service, and cost_usd columns")

        for line_number, row in enumerate(reader, start=2):
            service_value = row.get("service")
            date_value = row.get("date")
            cost_value = row.get("cost_usd")
            if not service_value or not date_value or not cost_value:
                raise ValueError(f"Missing value on CSV line {line_number}")

            try:
                usage_date = date.fromisoformat(date_value.strip())
                cost_usd = Decimal(cost_value.strip())
            except (ValueError, InvalidOperation) as error:
                raise ValueError(f"Invalid value on CSV line {line_number}") from error

            service = service_value.strip()
            if not service or not cost_usd.is_finite():
                raise ValueError(f"Invalid value on CSV line {line_number}")

            records.append(
                CostRecord(
                    usage_date=usage_date,
                    service=service,
                    cost_usd=cost_usd,
                )
            )

    return records


def summarize_costs(records: Iterable[CostRecord]) -> dict[str, object]:
    service_totals: defaultdict[str, Decimal] = defaultdict(Decimal)

    for record in records:
        service_totals[record.service] += record.cost_usd

    total_cost = sum(service_totals.values(), start=Decimal("0"))
    services = [
        {"service": service, "cost_usd": format(cost, "f")}
        for service, cost in sorted(
            service_totals.items(),
            key=lambda item: (-item[1], item[0]),
        )
    ]

    return {
        "currency": "USD",
        "source": "synthetic_sample",
        "total_cost_usd": format(total_cost, "f"),
        "services": services,
    }
