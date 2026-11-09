import unittest

from fastapi.testclient import TestClient

from backend.app.main import app


class ApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_health_endpoint(self) -> None:
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_cost_summary_endpoint_uses_synthetic_sample(self) -> None:
        response = self.client.get("/api/v1/costs/summary")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["source"], "synthetic_sample")
        self.assertEqual(response.json()["total_cost_usd"], "46.35")


if __name__ == "__main__":
    unittest.main()
