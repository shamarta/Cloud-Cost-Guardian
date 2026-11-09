# Cloud Cost Guardian

An AWS-first cloud-cost learning project. The first milestone is an educational API that summarizes **synthetic** cost data; it does not connect to AWS or represent a market-validated product.

## Current milestone

- FastAPI backend with a health endpoint and a cost-summary endpoint.
- Local CSV containing clearly labeled synthetic data.
- Unit and API tests.
- No AWS credentials, cloud account access, database, or billing integrations.

## Run locally

From the project root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m uvicorn backend.app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to explore the API, or `http://127.0.0.1:8000/api/v1/costs/summary` to see the sample summary.

Run tests:

```powershell
python -m pytest
```

## Learning sequence

1. Understand the API and test the sample cost summary.
2. Learn the AWS billing-data options and their delays, permissions, and cost implications.
3. Add a read-only AWS data import only after the local data flow is understood.
4. Revisit customer discovery before treating the prototype as a commercial product.

See [`docs/market-validation.md`](docs/market-validation.md) for the current unvalidated hypotheses and [`docs/customer-discovery-interviews.md`](docs/customer-discovery-interviews.md) for the deferred discovery plan.
