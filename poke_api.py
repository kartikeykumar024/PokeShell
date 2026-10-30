import requests

url = 'https://pokeapi.co/api/v2/pokemon/'


class PokemonData():
    
    def __init__(self, pokemon_name):
        
        self.moves_dict = {}
        
        self.pokemon_name = pokemon_name
        
        self.pokemon_data = requests.get(f"{url}{self.pokemon_name}").json()
                        
        self.x2_types = []
        self.half_types = []
        self.immune_types = []


    @staticmethod
    def loop_data1(relation_data, category):
        
        for i in range(0, len(relation_data)):
            category.append(relation_data[i]["name"])         
            

    def damage_relation(self, type_data):
        
        
        for relation_name, relation_dict in type_data["damage_relations"].items():
            
            if relation_name == "double_damage_from":
                self.loop_data1(relation_dict, self.x2_types)
                
                
            if relation_name == "half_damage_from":
                self.loop_data1(relation_dict, self.half_moves) 
                
            
            if relation_name == "no_damage_from":
                self.loop_data1(relation_dict, self.immune_moves)
                
                                
        
        
    def get_pokemon_stats(self):

        pokemon_data = requests.get(f"{url}{self.pokemon_name}").json()
        
        type1_url = pokemon_data["types"][0]["type"]["url"]
        type2_url =  pokemon_data["types"][1]["type"]["url"]
        
        type1_data = requests.get(type1_url).json()
        type2_data = requests.get(type2_url).json()

        type1 =  pokemon_data["types"][0]["type"]["name"]
        type2 =  pokemon_data["types"][1]["type"]["name"]
        
        self.damage_relation(type1_data)
        self.damage_relation(type2_data)
                
        
        self.max_hp =  pokemon_data["stats"][0]["base_stat"]
        self.hp =  pokemon_data["stats"][0]["base_stat"]
        self.attack = pokemon_data["stats"][1]["base_stat"]
        self.sp_atk = pokemon_data["stats"][1]["base_stat"]
        self.defense = pokemon_data["stats"][4]["base_stat"]
        self.sp_def = pokemon_data["stats"][5]["base_stat"]
        self.speed = pokemon_data["stats"][5]["base_stat"]
        self.type = [type1, type2]    



    def get_available_moves(self):

        available_moves = {}

        for moves in self.pokemon_data["moves"]:

            for fields in moves["version_group_details"]:

                if fields["version_group"]["name"] == "sword-shield":
                    if fields["move_learn_method"]["name"] == "level-up":
                
                        move_name = moves["move"]["name"]
                        move_url = moves["move"]["url"]

                        available_moves[move_name] = move_url

            if len(available_moves.keys()) == 8:
                break

        return available_moves


    def get_move_data(self, selected_moves):

        for name, url in selected_moves.items():

            move_data = requests.get(url).json()


            self.moves_dict[name] = {"power": move_data["power"],
                                "pp": move_data["pp"],
                                "accuracy": move_data["accuracy"],
                                "type": move_data["type"]["name"],
                                "dmg_class": move_data["damage_class"]["name"],
                                "ailment": move_data["meta"]["ailment"]["name"],
                                "alm_chance": move_data["meta"]["ailment_chance"]}