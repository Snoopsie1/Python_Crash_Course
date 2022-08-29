#Make a dictionary called cities.
# Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city
# and include the country that the city is in, its approx population, and one fact about the city.
# Print the name of each city and all the information you have stored about it.

cities = {
    "copenhagen": {
        "country": "denmark",
        "population": "2",
        "fact": "lots of bikes"
    },
    "tokyo": {
        "country": "japan",
        "population": "8",
        "fact": "lots of technology"
    },
    "lyngby" : {
        "country": "denmark",
        "population": "40",
        "fact": "lots of geeks"
    }
}

for city, fact in cities.items():
    print(f"\n{city.title()} : ")
    for key, value in fact.items():
        print(f"{key.title()} : {value.title()}")
