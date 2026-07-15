"""
Test Cases for Account Routes
"""
import unittest
from service import app, db
from service.models import Account


class TestAccountRoutes(unittest.TestCase):
    """Test cases for Account routes"""

    @classmethod
    def setUpClass(cls):
        """Set up test client"""
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        cls.client = app.test_client()
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Tear down test database"""
        with app.app_context():
            db.drop_all()

    def setUp(self):
        """Set up before each test"""
        with app.app_context():
            db.session.query(Account).delete()
            db.session.commit()

    def _create_account(self):
        """Helper to create a test account"""
        return self.client.post(
            "/accounts",
            json={
                "name": "John Doe",
                "email": "john@example.com",
                "address": "123 Main St",
                "phone": "555-1234",
            },
        )

    def test_health(self):
        """Test health endpoint"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)

    def test_create_account(self):
        """Test CREATE account"""
        resp = self._create_account()
        self.assertEqual(resp.status_code, 201)
        data = resp.get_json()
        self.assertEqual(data["name"], "John Doe")

    def test_list_accounts(self):
        """Test LIST accounts"""
        self._create_account()
        resp = self.client.get("/accounts")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertGreater(len(data), 0)

    def test_read_account(self):
        """Test READ account"""
        create_resp = self._create_account()
        account_id = create_resp.get_json()["id"]
        resp = self.client.get(f"/accounts/{account_id}")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["name"], "John Doe")

    def test_update_account(self):
        """Test UPDATE account"""
        create_resp = self._create_account()
        account_id = create_resp.get_json()["id"]
        resp = self.client.put(
            f"/accounts/{account_id}",
            json={
                "name": "Jane Doe",
                "email": "jane@example.com",
                "address": "456 Oak Ave",
                "phone": "555-5678",
            },
        )
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["name"], "Jane Doe")

    def test_delete_account(self):
        """Test DELETE account"""
        create_resp = self._create_account()
        account_id = create_resp.get_json()["id"]
        resp = self.client.delete(f"/accounts/{account_id}")
        self.assertEqual(resp.status_code, 204)

    def test_read_account_not_found(self):
        """Test READ account not found"""
        resp = self.client.get("/accounts/9999")
        self.assertEqual(resp.status_code, 404)

def test_cors_header(self):
    """Test CORS header is returned"""
    resp = self.client.get("/health")
    self.assertEqual(resp.status_code, 200)
    self.assertIn("Access-Control-Allow-Origin", resp.headers)

def test_security_headers(self):
    """Test security headers are returned"""
    resp = self.client.get("/health")
    self.assertIn("X-Frame-Options", resp.headers)
    self.assertIn("X-Content-Type-Options", resp.headers)


if __name__ == "__main__":
    unittest.main()
