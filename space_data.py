# 2. Exploring the Digital Cosmos
# Task 1 completed

# Task 2: Fetch Data from Space API

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue'] if planet['mass'] else 'Unknown'
            orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else 'Unknown'
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()