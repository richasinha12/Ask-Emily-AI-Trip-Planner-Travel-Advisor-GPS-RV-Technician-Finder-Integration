# utils/data_fetcher.py
import requests
from config import API_KEYS

def fetch_campground_data(location):
    # Example endpoint for campground data
    response = requests.get(f"https://examplecampgroundapi.com/{location}")
    return response.json()

def fetch_fuel_stations(route):
    google_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={route}&radius=5000&type=gas_station&key={API_KEYS['google_maps']}"
    response = requests.get(google_url)
    return response.json()

def fetch_bridge_clearance(route):
    # Simulate fetching bridge height data
    response = requests.get(f"https://govbridgeapi.com/{route}")
    return response.json()
