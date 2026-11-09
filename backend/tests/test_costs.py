from datetime import date
from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from backend.app.costs import CostRecord, read_cost_records, summarize_costs


class CostSummaryTests(unittest.TestCase):
    def test_summarize_costs_groups_services_and_preserves_decimal_precision(self) -> None:
        records = [
            CostRecord(date(2026, 11, 1), "Amazon EC2", Decimal("12.40")),
            CostRecord(date(2026, 11, 2), "Amazon EC2", Decimal("14.20")),
            CostRecord(date(2026, 11, 1), "Amazon S3", Decimal("1.10")),
        ]

        summary = summarize_costs(records)

        self.assertEqual(summary["total_cost_usd"], "27.70")
        self.assertEqual(
            summary["services"],
            [
                {"service": "Amazon EC2", "cost_usd": "26.60"},
                {"service": "Amazon S3", "cost_usd": "1.10"},
            ],
        )

    def test_read_cost_records_rejects_invalid_cost(self) -> None:
        with TemporaryDirectory() as temporary_directory:
            csv_path = Path(temporary_directory) / "costs.csv"
            csv_path.write_text(
                "date,service,cost_usd\n2026-11-01,Amazon EC2,not-a-cost\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "line 2"):
                read_cost_records(csv_path)


if __name__ == "__main__":
    unittest.main()
