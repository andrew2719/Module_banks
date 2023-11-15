# Map representation
map_data = {
    "cities": ["CityA", "CityB"],
    "roads": [("CityA", "CityB")],  # Road connecting CityA and CityB
    "rivers": {"River": ["CityA"]}  # River flows through CityA
}

# Function to display map information
def display_map_info():
    for city in map_data["cities"]:
        print(f"City: {city}")
        if any(city in road for road in map_data["roads"]):
            print(f"  - Connected by road")
        if city in map_data["rivers"]["River"]:
            print(f"  - River flows through this city")

# Display the map information
print("Map information:")
display_map_info()

# FOL Representation

def fol_representation():
    # Cities
    for city in map_data["cities"]:
        print(f"City({city})")

    # Road connections
    for road in map_data["roads"]:
        print(f"ConnectedByRoad({road[0]}, {road[1]})")

    # River flows
    for river, cities in map_data["rivers"].items():
        for city in cities:
            print(f"FlowsThrough({river}, {city})")

# Display the FOL representation
print("\nFOL representation:")
fol_representation()
