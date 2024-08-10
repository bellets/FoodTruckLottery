import csv
import random
import argparse
import requests

# Function to read and parse the CSV file
def read_csv(file_path):
    food_trucks = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            food_trucks.append({
                "name": row["Applicant"],
                "food_type": row["FoodItems"],
                "location": (float(row["Latitude"]), float(row["Longitude"])),
                "operating_hours": row["dayshours"]
            })
    return food_trucks

# Function to filter food trucks based on user input
def filter_food_trucks(food_trucks, food_type=None):
    filtered_trucks = food_trucks
    if food_type:
        filtered_trucks = [truck for truck in filtered_trucks if food_type.lower() in truck["food_type"].lower()]
    return filtered_trucks

# Function to select a random food truck from the filtered list
def select_random_food_truck(filtered_trucks):
    if not filtered_trucks:
        return None
    return random.choice(filtered_trucks)

# Function to get a list of 10 food trucks for a particular cuisine
def get_food_trucks_list(filtered_trucks, count=10):
    return random.sample(filtered_trucks, min(count, len(filtered_trucks)))

# Function to get a more intuitive address using Google Maps API
def get_address_from_location(location, api_key):
    if not api_key:
        return f"Lat: {location[0]}, Lng: {location[1]}"
    
    lat, lng = location
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get("results")
        if results:
            return results[0].get("formatted_address")
    return "Address not found"

# Main function to handle command-line arguments and run the lottery
def main():
    parser = argparse.ArgumentParser(description="Food Truck Lottery System")
    parser.add_argument("--file", type=str, required=True, help="Path to the CSV file")
    parser.add_argument("--food_type", type=str, help="Filter by food type")
    parser.add_argument("--list", action="store_true", help="Get a list of 10 food trucks for the specified cuisine")
    parser.add_argument("--api_key", type=str, help="Google Maps API key (optional)")
    args = parser.parse_args()

    # Read and process the CSV file
    food_trucks = read_csv(args.file)

    # Filter food trucks based on user input
    filtered_trucks = filter_food_trucks(food_trucks, food_type=args.food_type)

    if args.list:
        # Get a list of 10 food trucks for the specified cuisine
        food_trucks_list = get_food_trucks_list(filtered_trucks)
        for truck in food_trucks_list:
            address = get_address_from_location(truck["location"], args.api_key)
            print(f"Food Truck: {truck['name']}")
            print(f"Food Type: {truck['food_type']}")
            print(f"Location: {address}")
            print(f"Operating Hours: {truck['operating_hours']}")
            print()
    else:
        # Select a random food truck from the filtered list
        selected_truck = select_random_food_truck(filtered_trucks)
        if selected_truck:
            address = get_address_from_location(selected_truck["location"], args.api_key)
            print(f"Selected Food Truck: {selected_truck['name']}")
            print(f"Food Type: {selected_truck['food_type']}")
            print(f"Location: {address}")
            print(f"Operating Hours: {selected_truck['operating_hours']}")
        else:
            print("No food trucks found matching the criteria.")

if __name__ == "__main__":
    main()


