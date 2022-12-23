import json
import os

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_cors import CORS, cross_origin

from services.lunch import get_today_lunch, add_lunch
from services.restaurant import get_all_restaurants
from url_registry import UrlRegistry
from url_dispatch_table import UrlDispatchTable

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


crawling_interval = os.environ['CRAWLER_INTERVAL_MIN'] if 'CRAWLER_INTERVAL_MIN' in os.environ else 1
scheduler = BackgroundScheduler()
scheduler.start()

registry = UrlRegistry()
dispatch_table = UrlDispatchTable(registry)
dispatch_table()


@scheduler.scheduled_job('interval', minutes=crawling_interval)
def scheduled_job():
    global registry
    global dispatch_table
    registry = UrlRegistry()
    dispatch_table = UrlDispatchTable(registry)
    dispatch_table()
    print("This job is executed every minute.")


@app.route('/lunch', methods=['GET'])
@cross_origin()
def route_get_lunch():
    global dispatch_table
    return json.dumps(dispatch_table(), default=vars)


@app.route('/v1/lunch', methods=['GET'])
@cross_origin()
def route_today_lunch():
    return json.dumps(get_today_lunch(), default=vars)


@app.route('/v1/lunch/<restaurant_id>', methods=['POST'])
@cross_origin()
def route_add_lunch(restaurant_id, menu):
    print("add: " + restaurant_id)
    add_lunch(restaurant_id, menu)


@app.route('/v1/restaurant', methods=['GET'])
@cross_origin()
def route_get_restaurant():
    return json.dumps(get_all_restaurants(), default=vars)
