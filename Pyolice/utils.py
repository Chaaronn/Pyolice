

def validate_lat_lng(lat: float, lng: float):
    """Validate latitude and longitude values."""
    if not (-90 <= lat <= 90 and -180 <= lng <= 180):
        raise ValueError("Latitude must be between -90 and 90, and longitude must be between -180 and 180.")


def validate_polygon(poly: str):
    """Validate polygon string."""
    if not isinstance(poly, str) or not poly:
        raise ValueError("Polygon must be a non-empty string.")
