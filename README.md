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

Pyolice is split between 4 sections
- Street level crimes
- Neighbourhood
- Stop and search
- Police force

Here are some examples of how to use Pyolice:

### Street Level Crimes

#### Fetching Crimes at a Specific Location
```python
import pyolice

crimes = pyolice.street_level.get_street_crimes_at_location(lat=52.629729, lng=-1.131592)
print(crimes)
```

#### Fetching Crimes in a Custom Area
```python
import pyolice

polygon = "52.268,0.543:52.794,0.238:52.130,0.478"
crimes = pyolice.street_level.get_street_crimes_in_area(poly=polygon)
print(crimes)
```

#### Fetching Outcomes at a Specific Location
```python
import pyolice

outcomes = pyolice.street_level.get_outcomes_at_location(location_id="12345", date="2023-12")
print(outcomes)
```

#### Fetching Outcomes by Coordinates
```python
import pyolice

outcomes = pyolice.street_level.get_outcomes_by_coordinates(lat=52.629729, lng=-1.131592, date="2023-12")
print(outcomes)
```

#### Fetching Outcomes in a Custom Area
```python
import pyolice

polygon = "52.268,0.543:52.794,0.238:52.130,0.478"
outcomes = pyolice.street_level.get_outcomes_in_area(poly=polygon)
print(outcomes)
```

#### Fetching Crimes at a Specific Location by ID or Coordinates
```python
import pyolice

# Fetch by location ID
crimes = pyolice.street_level.get_crimes_at_specific_location(location_id="12345")
print(crimes)

# Fetch by coordinates
crimes = pyolice.street_level.get_crimes_at_specific_location(lat=52.629729, lng=-1.131592)
print(crimes)
```

#### Fetching Crimes with No Location
```python
import pyolice

crimes = pyolice.street_level.get_crimes_no_location(category="all-crime", force="leicestershire", date="2023-12")
print(crimes)
```

#### Fetching Crime Categories
```python
import pyolice

categories = pyolice.street_level.get_crime_categories(date="2023-12")
print(categories)
```

#### Fetching Last Updated Date
```python
import pyolice

last_updated = pyolice.street_level.get_last_updated()
print(last_updated)
```

#### Fetching Outcomes for a Specific Crime
```python
import pyolice

crime_id = "e11dade0a92a912d12329b9b2abb856ac9520434ad6845c30f503e9901d140f1"
outcomes = pyolice.street_level.get_outcomes_for_crime(crime_id=crime_id)
print(outcomes)
```
### Fetching Neighbourhood Details
```python
import pyolice

neighbourhoods = pyolice.neighbourhoods.list_neighbourhoods(force_id="leicestershire")
print(neighbourhoods)
```

### Stop and Search
```python
import pyolice

stops = pyolice.stop_search.stop_and_search_by_force(force="leicestershire", date="2023-12")
print(stops)
```

### Fetching Police Force Details
```python
import pyolice

forces = pyolice.forces.list_forces()
print(forces)
```

## Validation
Pyolice provides built-in validation for inputs:
- Latitude and longitude are validated to ensure they fall within valid ranges.
- Polygon strings for custom areas are checked for proper formatting.

## Acknowledgements
This project relies on the [UK Police API](https://data.police.uk/docs/) for data access and services.