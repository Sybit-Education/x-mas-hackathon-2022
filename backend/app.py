import json

from flask import Flask
from services.restaurant import get_all_restaurants
from url_registry import UrlRegistry
from url_dispatch_table import UrlDispatchTable

app = Flask(__name__)
registry = UrlRegistry()
dispatch_table = UrlDispatchTable(registry)
dispatch_table()


@app.route('/lunch', methods=['GET'])
def route_get_lunch():
    return json.dumps(dispatch_table(), default=vars)


@app.route('/restaurant', methods=['GET'])
def route_get_restaurant():
    return json.dumps(get_all_restaurants(), default=vars)
