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
    f = open("../k8s/my-app/files/visits-list.txt", "a")
    f.write(current_time.strftime(TIME_FORMAT)+"/n")
    f.close()
    return render_template('time_template.html',
                           time=current_time.strftime(TIME_FORMAT))

@app.route('/visits')
def visits():
    f = open("../k8s/my-app/files/visits-list.txt", "r")
    text = f.read()
    return render_template('visits_template.html',
                           visits=text) 


def get_timezone_from_utc(utc):
    if utc > -24 and utc < 24:
        return datetime.timezone(datetime.timedelta(hours=utc))
    else:
        return None


if __name__ == '__main__':
    app.run()
