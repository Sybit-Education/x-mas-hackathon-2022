from flask import Flask
from endpoints.country import get_countries

app = Flask(__name__)


@app.route('/country', methods=['GET'])
def route_get_countries():
    return get_countries()
