from Pyolice.client import Pyolice
from Pyolice.utils import validate_lat_lng, validate_polygon

class StreetLevelCrime:
    def __init__(self):
        self.client = Pyolice()

    def get_crimes_at_location(self, lat: float, lng: float, date: str = None):
        """
        Retrieve crimes at a specific location.
        
        :param lat: Latitude of the location.
        :param lng: Longitude of the location.
        :param date: (Optional) Date in YYYY-MM format. Defaults to the latest month.
        :return: List of crimes at the given location.
        :raises: ValueError for invalid inputs, APIError for request failures.
        """
        # validate given is correct
        validate_lat_lng(lat, lng)

        params = {"lat": lat, "lng": lng}

        # As date is optional
        if date:
            params["date"] = date


        return self.client._get("crimes-street/all-crime", params=params)

    def get_crimes_in_area(self, poly: str, date: str = None):
        """
        Retrieve crimes in a specific custom area.
        
        :param poly: The lat/lng pairs defining the area boundary (format: [lat,lng]:[lat,lng]).
        :param date: (Optional) Date in YYYY-MM format. Defaults to the latest month.
        :return: List of crimes in the specified area.
        :raises: ValueError for invalid inputs, APIError for request failures.
        """
        # validate its correct
        validate_polygon(poly)

        params = {"poly": poly}
        if date:
            params["date"] = date
            
        return self.client._get("crimes-street/all-crime", params=params)

client = StreetLevelCrime()
data = client.get_crimes_at_location(52.629729, -1.131592)
print()