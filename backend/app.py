import json
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from services.lunch import get_today_lunch, add_lunch
from services.restaurant import get_all_restaurants
from url_registry import UrlRegistry
from url_dispatch_table import UrlDispatchTable

app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.start()

registry = UrlRegistry()
dispatch_table = UrlDispatchTable(registry)
dispatch_table()


@scheduler.scheduled_job('interval', minutes=1)
def scheduled_job():
    print("This job is run every minute.")


@app.route('/lunch', methods=['GET'])
def route_get_lunch():
    return json.dumps(dispatch_table(), default=vars)


@app.route('/v1/lunch', methods=['GET'])
def route_today_lunch():
    return json.dumps(get_today_lunch(), default=vars)


@app.route('/v1/lunch/<restaurant_id>', methods=['POST'])
def route_add_lunch(restaurant_id, menu):
    print("add: " + restaurant_id)
    add_lunch(restaurant_id, menu)


@app.route('/v1/restaurant', methods=['GET'])
def route_get_restaurant():
    return json.dumps(get_all_restaurants(), default=vars)
