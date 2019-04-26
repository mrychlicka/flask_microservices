from services import root_dir, nice_json
from flask import Flask
import json
import requests

app = Flask(__name__)


with open("{}/dbs/passengers".format(root_dir()), 'r') as a:
    passengers = json.load(a)


@app.route('/')
def hello():
    response_data = "Hi!\n" \
                    "What do you want to do here?\n" \
                    "* /passengers - all passengers info\n" \
                    "* /passengers/<passenger> - specific passenger info\n" \
                    "* /passengers/<passenger>/flight' - number of flight passenger is booked\n" \
                    "* /passengers/<passenger>/flight/info - passenger flight info"
    return response_data


@app.route('/passengers', methods=['GET'])
def get_all_passengers():
    return nice_json(passengers)


@app.route('/passengers/<passenger>')
def get_passenger_info(passenger):
    return nice_json(passengers[passenger])


@app.route('/passengers/<passenger>/flight', methods=['GET'])
def get_passenger_flights(passenger):
    return nice_json(passengers[passenger]["flight"])


@app.route('/passengers/<passenger>/flight/info', methods=['GET'])
def get_passenger_specific_flight(passenger):
    passenger_flight = passengers[passenger]["flight"]
    response = requests.get("http://127.0.0.1:5001/flights/{}".format(passenger_flight)).json()
    return nice_json(response)


if __name__ == "__main__":
    app.run(port=5002, debug=True)
