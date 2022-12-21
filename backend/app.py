import json

from flask import Flask
from endpoints.country import get_countries
from url_registry import UrlRegistry
from url_dispatch_table import UrlDispatchTable

app = Flask(__name__)
registry = UrlRegistry()
dispatch_table = UrlDispatchTable(registry)
dispatch_table()


@app.route('/lunch', methods=['GET'])
def route_get_lunch():
    return json.dumps(dispatch_table(), default=vars)
