import unittest
import app as tested_app
import datetime

class AppTests(unittest.TestCase):

    def test_utc(self):
        test_cases = [-1000, -24, -23, -11, -3, 5, 13, 23, 24, 1000]
        for test_utc in test_cases:
            result = tested_app.get_timezone_from_utc(test_utc)
            if test_utc >= 24 or test_utc <= -24:
                self.assertEqual(result, nil)
            else:
                self.assertEqual(result, datetime.timezone(
                        datetime.timedelta(hours=test_utc)))


if __name__ == '__main__':
    unittest.main()
