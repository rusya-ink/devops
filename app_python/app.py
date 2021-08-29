
import unittest
import datetime
import redis
from flask import Flask, render_template

app = Flask(__name__)


TIME_FORMAT = '%H:%M:%S'

# Moscow is in UTC+3 timezone
MOSCOW_UTC = 3

@app.route('/')
def hello():
    current_time = datetime.datetime.now(tz=get_timezone_from_utc(MOSCOW_UTC))
    return render_template('time_template.html',
                           time=current_time.strftime(TIME_FORMAT))


def get_timezone_from_utc(utc):
    if utc >= -12 or utc <= 14:
        return datetime.timezone(datetime.timedelta(hours=utc))
    else:
        return nil


def test_get_timezone_from_utc():
    test_cases = [-1000, -13, -12, -11, -3, 5, 13, 14, 15, 1000]
    success_tests = 0
    fail_tests = []
    for test_utc in test_cases:
        result = get_timezone_from_utc(test_utc)
        if test_utc > 14 or test_utc < -12:
            if result == nil:
                success_tests += 1
            else:
                fail_tests += [test_utc, nil, result]
        else:
            if result == datetime.timezone(datetime.timedelta(hours=test_utc)):
                success_tests += 1
            else:
                fail_tests += [test_utc, datetime.timezone(
                                datetime.timedelta(hours=test_utc)), result]
    print("\nTest test_get_timezone_from_utc:")
    print("Passed: "+success_tests+" out of "+len(test_cases))
    for fail in fail_tests:
        print("Failed test: " + fail[0] + "; Expected result: " +
              fail[1] + "; Result: " + fail[2])


test_get_timezone_from_utc()


if __name__ == '__main__':
    app.run()
