# Pyolice

Pyolice is a Python wrapper for the UK Police API. It allows developers to easily access various endpoints of the API, including street-level crimes and other police data.

## Features
- Fetch street-level crimes for a specific location or custom area.
- Validate input parameters like latitude, longitude, and polygon strings.
- Handle API errors gracefully.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/pyolice.git
   ```

2. Navigate to the project directory:
   ```bash
   cd pyolice
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Example: Fetch Crimes at a Specific Location

The `get_crimes_at_location` method retrieves crimes at a specific location based on latitude and longitude. Optionally, you can provide a date in `YYYY-MM` format to limit the results to a specific month.

#### Code Example:

```python
from Pyolice.endpoints import StreetLevelCrime

# Initialize the StreetLevelCrime client
client = StreetLevelCrime()

# Fetch crimes at a specific location
latitude = 52.629729
longitude = -1.131592
data = client.get_crimes_at_location(latitude, longitude, date="2024-01")

# Print the result
print(data)
```

#### Parameters:
- `lat` (float): Latitude of the location.
- `lng` (float): Longitude of the location.
- `date` (str, optional): Date in `YYYY-MM` format. Defaults to the latest available month.

#### Returns:
- A list of crime data at the specified location.

### Example: Fetch Crimes in a Custom Area

The `get_crimes_in_area` method retrieves crimes in a custom-defined area using a polygon string.

#### Code Example:

```python
from Pyolice.endpoints import StreetLevelCrime

# Initialize the StreetLevelCrime client
client = StreetLevelCrime()

# Define a polygon area (format: [lat,lng]:[lat,lng])
polygon = "52.268,0.543:52.794,0.238:52.130,0.478"
data = client.get_crimes_in_area(polygon, date="2024-01")

# Print the result
print(data)
```

#### Parameters:
- `poly` (str): A polygon string defining the area boundary.
- `date` (str, optional): Date in `YYYY-MM` format. Defaults to the latest available month.

#### Returns:
- A list of crime data within the specified area.

## Error Handling

Pyolice uses custom exceptions to handle errors:
- `APIError`: Raised for API request failures.
- `ValueError`: Raised for invalid input parameters.

## License
This project is licensed under the MIT License.
