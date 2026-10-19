import os
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app


class ApplicationTests(unittest.TestCase):
    def test_root_returns_student_information(self):
        with patch.dict(os.environ, {}, clear=True), TestClient(app) as client:
            response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["student"], {
            "name": "Alexandr",
            "surname": "Sgibnev",
            "group": "IT2-2314",
            "student_id": "37882",
        })
        self.assertEqual(response.json()["course"], "DevOps")
        self.assertEqual(
            response.json()["message"], "Application is running successfully!"
        )

    def test_environment_overrides_defaults(self):
        settings = {
            "STUDENT_NAME": "Test",
            "STUDENT_SURNAME": "User",
            "STUDENT_GROUP": "TEST-0000",
            "STUDENT_ID": "00000",
        }
        with patch.dict(os.environ, settings), TestClient(app) as client:
            response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["student"], {
            "name": "Test",
            "surname": "User",
            "group": "TEST-0000",
            "student_id": "00000",
        })

    def test_only_root_is_available(self):
        with TestClient(app) as client:
            for path in ("/docs", "/redoc", "/openapi.json", "/missing"):
                with self.subTest(path=path):
                    self.assertEqual(client.get(path).status_code, 404)


if __name__ == "__main__":
    unittest.main()
