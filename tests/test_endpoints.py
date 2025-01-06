import unittest
from unittest.mock import MagicMock
from Pyolice.endpoints import StreetLevelCrime
from Pyolice.client import Pyolice
from Pyolice.exceptions import APIError

class TestStreetLevelCrime(unittest.TestCase):
    def setUp(self):
        self.api_client = Pyolice()
        self.api_client._get = MagicMock()
        self.crime_endpoint = StreetLevelCrime(self.api_client)

    def test_get_crimes_at_location_success(self):
        # Mock response
        mock_response = [{"category": "anti-social-behaviour", "id": 123}]
        self.api_client._get.return_value = mock_response

        # Call the method
        response = self.crime_endpoint.get_crimes_at_location(52.629729, -1.131592, "2024-01")
        
        # Assertions
        self.api_client._get.assert_called_once_with(
            "crimes-street/all-crime", {"lat": 52.629729, "lng": -1.131592, "date": "2024-01"}
        )
        self.assertEqual(response, mock_response)

    def test_get_crimes_in_area_success(self):
        # Mock response
        mock_response = [{"category": "bicycle-theft", "id": 456}]
        self.api_client._get.return_value = mock_response

        # Call the method
        poly = "52.268,0.543:52.794,0.238:52.130,0.478"
        response = self.crime_endpoint.get_crimes_in_area(poly, "2024-01")
        
        # Assertions
        self.api_client._get.assert_called_once_with(
            "crimes-street/all-crime", {"poly": poly, "date": "2024-01"}
        )
        self.assertEqual(response, mock_response)

    def test_get_crimes_at_location_invalid_lat_lng(self):
        with self.assertRaises(ValueError):
            self.crime_endpoint.get_crimes_at_location(100.0, 200.0)

    def test_get_crimes_in_area_invalid_poly(self):
        with self.assertRaises(ValueError):
            self.crime_endpoint.get_crimes_in_area("invalid_polygon_string")

    def test_api_error_handling(self):
        self.api_client._get.side_effect = APIError("API error occurred")
        with self.assertRaises(APIError):
            self.crime_endpoint.get_crimes_at_location(52.629729, -1.131592)
