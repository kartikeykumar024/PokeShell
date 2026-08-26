import requests

url = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_data(pokemon_name):

    pokemon = requests.get(f"{url}{pokemon_name}").json()

    pokemon_data = {"name" : pokemon_name,
                     "hp": pokemon["stats"][0]["base_stat"],
                     "atk": pokemon["stats"][1]["base_stat"],
                     "sp. atk": pokemon["stats"][1]["base_stat"],
                     "def": pokemon["stats"][4]["base_stat"],
                     "sp. def": pokemon["stats"][4]["base_stat"],
                     "speed": pokemon["stats"][5]["base_stat"],

                     "moves": [
                     ]}

    print(pokemon_data)




    return pokemon_data



get_pokemon_data("pikachu")