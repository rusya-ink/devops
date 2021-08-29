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
    if utc > -24 and utc < 24:
        return datetime.timezone(datetime.timedelta(hours=utc))
    else:
        return null


if __name__ == '__main__':
    app.run()
