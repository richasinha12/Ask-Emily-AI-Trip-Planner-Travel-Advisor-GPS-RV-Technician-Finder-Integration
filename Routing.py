 RV-Specific Routing 
Use Google Maps to generate RV routes based on vehicle height and weight.

# utils/routing.py
import googlemaps
from config import API_KEYS

gmaps = googlemaps.Client(key=API_KEYS["google_maps"])

def get_rv_route(start, destination, rv_specs):
    route = gmaps.directions(start, destination, avoid=["tolls", "ferries"])
    # Filter route steps based on RV clearance and bridge heights
    route_filtered = [step for step in route if check_clearance(step, rv_specs)]
    return route_filtered

def check_clearance(route_step, rv_specs):
    # Simple height check based on RV specifications
    return True if route_step.get('height', float('inf')) >= rv_specs['height'] else False
