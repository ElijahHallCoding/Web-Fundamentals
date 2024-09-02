# Task 3: Analyzing and Displaying Data

import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {pokemon_name}")
        return None

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight += pokemon['weight']
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data = []

for name in pokemon_names:
    data = fetch_pokemon_data(name)
    if data:
        pokemon_data.append(data)
        print(f"\nName: {data['name'].title()}")
        print("Abilities:")
        for ability in data['abilities']:
            print(f"- {ability['ability']['name']}")

average_weight = calculate_average_weight(pokemon_data)
print(f"\nThe average weight of the Pokémon is {average_weight} hectograms.")