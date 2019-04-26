from flask import Flask
import requests
import json

from services import root_dir, nice_json

app = Flask(__name__)

with open('{}/dbs/flight_dates'.format(root_dir()), 'r') as f:
    flight_dates = json.load(f)


@app.route('/')
def hello():
    return "Hey!\n" \
           "What do you want to know?\n" \
           "/dates - list of all flights\n" \
           "/dates/<date> - lists on flights on given day\n" \
           "/dates/<date>/flights_info - info about flights on specific date"


@app.route('/dates', methods=['GET'])
def get_all_flights():
    return nice_json(flight_dates)


@app.route('/dates/<date>', methods=['GET'])
def get_all_flights_from_date(date):
    return nice_json(flight_dates[date])


@app.route('/dates/<date>/flights_info')
def get_given_date_flights_info(date):
    which_date = flight_dates[date]
    print("+++++++++++ {}".format(which_date))
    response = {}
    for flight in which_date:
        response[flight] = requests.get("http://127.0.0.1:5001/flights/{}".format(flight)).json()
    return nice_json(response)


if __name__ == "__main__":
    app.run(port=5003, debug=True)
