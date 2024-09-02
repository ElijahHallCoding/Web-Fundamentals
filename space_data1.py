# Task: 3 Data Presentation and Analysis
 
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    return response.json()['bodies']

def find_heaviest_planet(planets):
    heaviest_planet = None
    max_mass = 0

    for planet in planets:
        if planet['isPlanet'] and planet['mass']:
            mass = planet['mass']['massValue']
            if mass > max_mass:
                max_mass = mass
                heaviest_planet = planet['englishName']
    return heaviest_planet, max_mass

planets = fetch_planet_data()
heaviest_planet, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {heaviest_planet} with a mass of {mass} kg.")
