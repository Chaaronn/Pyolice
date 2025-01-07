# Pyolice

## Overview
Pyolice is a Python wrapper for the UK Police API, providing an easy-to-use interface to access and interact with police data such as street-level crimes, outcomes, neighbourhoods, and stop-and-search activities. This readme.md is generated through ChatGPT for now, please forgive errors.

## Features
- Retrieve street-level crimes at specific locations or within custom areas.
- Fetch crime outcomes by coordinates, location, or area.
- Access information about neighbourhoods, including teams, events, and boundaries.
- Perform stop-and-search queries by area, force, or location.
- List and get details of police forces.
- Obtain metadata, such as available crime categories and the last updated date for the data.

## Requirements
- Python 3.7 or later
- `requests`

## Usage

Here are some examples:

### Fetching Crimes at a Specific Location
```python
from Pyolice.street_level import StreetLevelCrime

client = StreetLevelCrime()
crimes = client.get_street_crimes_at_location(lat=52.629729, lng=-1.131592)
print(crimes)
```

### Fetching Neighbourhood Details
```python
from Pyolice.neighbourhoods import Neighbourhoods

neighbourhood_client = Neighbourhoods()
neighbourhoods = neighbourhood_client.list_neighbourhoods(force_id="leicestershire")
print(neighbourhoods)
```

### Stop and Search by Force
```python
from Pyolice.stop_search import StopSearch

stop_search_client = StopSearch()
stops = stop_search_client.stop_and_search_by_force(force="leicestershire", date="2023-12")
print(stops)
```

### Fetching Police Force Details
```python
from Pyolice.forces import Forces

forces_client = Forces()
forces = forces_client.list_forces()
print(forces)
```

## Validation
Pyolice provides built-in validation for inputs:
- Latitude and longitude are validated to ensure they fall within valid ranges.
- Polygon strings for custom areas are checked for proper formatting.

## Acknowledgements
This project relies on the [UK Police API](https://data.police.uk/docs/) for data access and services.
