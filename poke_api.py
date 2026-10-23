import requests

url = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_stats(pokemon_name):

    pokemon_data = requests.get(f"{url}{pokemon_name}").json()    

    pokemon_stats = {"name" : pokemon_name,
                     "hp": pokemon_data["stats"][0]["base_stat"],
                     "atk": pokemon_data["stats"][1]["base_stat"],
                     "sp. atk": pokemon_data["stats"][1]["base_stat"],
                     "def": pokemon_data["stats"][4]["base_stat"],
                     "sp. def": pokemon_data["stats"][4]["base_stat"],
                     "speed": pokemon_data["stats"][5]["base_stat"],
                    }

    return pokemon_stats, pokemon_data


def get_available_moves(pokemon_stats, pokemon_data):

    available_moves = {}

    for moves in pokemon_data["moves"]:

        for fields in moves["version_group_details"]:

            if fields["version_group"]["name"] == "sword-shield":
                if fields["move_learn_method"]["name"] == "level-up":
            
                    move_name = moves["move"]["name"]
                    move_url = moves["move"]["url"]

                    available_moves[move_name] = move_url

        if len(available_moves.keys()) == 8:
            break

    return available_moves


def get_move_data(selected_moves):

    moves_dict = {}
    for name, url in selected_moves.items():


        move_data = requests.get(url).json()

        moves_dict[name] = {"power": move_data["power"],
                            "pp": move_data["pp"],
                            "accuracy": move_data["accuracy"],
                            "type": move_data["type"]["name"],
                            "dmg_class": move_data["damage_class"]["name"],
                            "ailment": move_data["meta"]["ailment"]["name"],
                            "alm_chance": move_data["meta"]["ailment_chance"]}
        


    return moves_dict

pokemon_stats, pokemon_data = get_pokemon_stats("charizard")
available_moves = get_available_moves(pokemon_stats, pokemon_data)
moves_dict = get_move_data(available_moves)
print(moves_dict)