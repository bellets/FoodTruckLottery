# Food Truck Lottery

## Description

The Food Truck Lottery is a command-line application that allows users to filter food trucks based on certain criteria and randomly selects a food truck from the filtered list. Additionally, the system can return a list of 10 food trucks for a particular cuisine and provide more intuitive location information using the Google Maps API.

## Features

- Filter food trucks by food type.
- Select a random food truck from the filtered list.
- Get a list of 10 food trucks for a particular cuisine.
- (Optional) Convert latitude and longitude into a more intuitive address using the Google Maps API.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)
- Google Maps API key

## Installation

1. Clone the repository or download the script.
2. Install the required Python libraries:
   `pip install requests`

## Examples
**Basic Run**: Select a random food truck from the entire list.
`python foodTruckLottery.py --file Mobile_Food_Facility_Permit.csv`

**Filter by Food Type**: Select a random food truck that serves tacos.
`python foodTruckLottery.py --file Mobile_Food_Facility_Permit.csv --food_type tacos --api_key YOUR_GOOGLE_MAPS_API_KEY`

**Get a List of 10 Food Trucks for a Particular Cuisine**: Get a list of 10 food trucks that serve Mexican food.
`python foodTruckLottery.py --file Mobile_Food_Facility_Permit.csv --food_type Mexican --list --api_key YOUR_GOOGLE_MAPS_API_KEY`
