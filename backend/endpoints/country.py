import json

import jsonify as jsonify

# A list of countries
countries = [
    {'name': 'Australia'},
    {'name': 'Canada'},
    {'name': 'France'},
    {'name': 'Germany'},
    {'name': 'Japan'},
    {'name': 'United Kingdom'},
    {'name': 'United States'},
]

# A route to return all of the countries
def get_countries():
    return json.dumps({'countries': countries})