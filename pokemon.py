# Task 1 completed.

# Task 2 Fetching Data

import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {pokemon_name}")
        return None

data = fetch_pokemon_data("pikachu")
if data:
    print(f"Name: {data['name'].title()}")
    print("Abilities:")
    for ability in data['abilities']:
        print(f"- {ability['ability']['name']}")

