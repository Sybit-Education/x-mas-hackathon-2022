import json

# A route to return all of the countries
def get_countries():
    return json.dumps({'countries': countries})