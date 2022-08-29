#Make a dictionary called favorite_places.
# Think of three names to use as keys in the dictionary,
# and store one to three favorite places for each person.
# Loop through the dictionary, and print each person's name and their favorite places.

favorite_places = {
    "bean": ["fælled-parken", "amager-strand", "pasha's kebab"],
    "nikolaj": ["bornholm", "lyngby"],
    "cleve": ["netto", "irma", "rema1000", "meny", "fakta", "super brugsen"],
    "galler": ["summoner's rift", "azeroth"]
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places:")
    for place in places:
        print(f"\t{place.title()}")