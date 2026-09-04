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
                    }

    return pokemon_data, pokemon


def get_available_moves(pokemon_data, pokemon):

    available_moves = {}

    for moves in pokemon["moves"]:

        for fields in moves["version_group_details"]:

            if fields["version_group"]["name"] == "sword-shield":
                if fields["move_learn_method"]["name"] == "level-up":
            
                    move_name = moves["move"]["name"]
                    move_url = moves["move"]["url"]

                    available_moves[move_name] = move_url


    return available_moves


def get_move_data(selected_moves):

    for name, url in selected_moves.items():

        move_details = requests.get(url)


    return move_details

get_pokemon_data("pikachu")