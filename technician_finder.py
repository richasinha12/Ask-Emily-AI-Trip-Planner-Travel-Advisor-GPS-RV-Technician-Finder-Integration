# utils/technician_finder.py
def get_rv_technicians(location):
    response = requests.get(f"https://rvtaaapi.com/technicians?location={location}")
    return response.json()
