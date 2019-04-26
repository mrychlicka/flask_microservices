from flask import Flask
import json

from services import root_dir, nice_json

app = Flask(__name__)

with open('{}/dbs/flights'.format(root_dir()), 'r') as f:
    flights = json.load(f)


@app.route('/')
def hello():
    response_data = "Hello!\n" \
                    "Things to do here:\n" \
                    "* /flights - all flights info\n" \
                    "* /flights/<flight> - specific flight info"

    return response_data


@app.route('/flights', methods=['GET'])
def get_all_flights():
    return nice_json(flights)


@app.route('/flights/<flight>', methods=['GET'])
def get_flight_info(flight):
    return nice_json(flights[flight])


if __name__ == '__main__':
    app.run(port=5001, debug=True)
