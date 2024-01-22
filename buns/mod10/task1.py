import requests
import json

def get_ship_info(ship_name):
    url = f"https://swapi.dev/api/starships/?search={ship_name}"
    response = requests.get(url)
    data = response.json()

    if data['count'] == 0:
        print(f"Ship {ship_name} not found.")
        return None
    
    ship_url = data['results'][0]['url']
    ship_data = requests.get(ship_url).json()
    return ship_data

def get_character_info(character_url):
    character_data = requests.get(character_url).json()
    homeworld_url = character_data['homeworld']
    homeworld_data = requests.get(homeworld_url).json()

    character_info = {
        'name': character_data['name'],
        'height': character_data['height'],
        'mass': character_data['mass'],
        'homeworld': homeworld_data['name'],
        'homeworld_url': homeworld_url
    }
    return character_info

def main():
    ship_name = "X-wing"
    ship_info = get_ship_info(ship_name)

    if ship_info:
        pilots_info = []
        for pilot_url in ship_info['pilots']:
            pilot_info = get_character_info(pilot_url)
            pilots_info.append(pilot_info)

        ship_data = {
            'ship_name': ship_info['name'],
            'max_atmosphering_speed': ship_info['max_atmosphering_speed'],
            'stership_class': ship_info['starship_class'],
            'pilots': pilots_info
        }

        print(json.dumps(ship_data, indent=4))

        with open('millennium_falcon_info.json', 'w') as file:
            json.dump(ship_data, file, indent=4)
    else:
        print("Ship information not found.")

if __name__ == "__main__":
    main()
