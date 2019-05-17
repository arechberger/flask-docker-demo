import main
import unittest
from unittest import mock


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()

    def test_home_page(self):
        home_page = self.app.get("/")
        self.assertEqual(
            home_page.data.decode("utf-8"), "Hello, World! This is version: 0.0.3"
        )

    def test_host_name_base(self):
        host_name = self.app.get("/hostname")
        self.assertTrue(
            host_name.data.decode("utf-8").startswith("You are on host"),
            msg=host_name.data.decode("utf-8"),
        )

    @mock.patch("os.getenv", return_value="TESTHOST")
    def test_hostname_full(self, mocked_getenv):
        host_name = self.app.get("/hostname")
        self.assertEqual(
            host_name.data.decode("utf-8"),
            "You are on host TESTHOST",
            msg=host_name.data.decode("utf-8"),
        )


if __name__ == "__main__":
    unittest.main()
