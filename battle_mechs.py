from random import randint   

##############            HELPER FUNCTIONS            ####################

def _type_iteration(type_list, value, type_to_check, multiplier):
        
        for type in list:    
            if type == type_to_check:
                
                multiplier *= value
                
                
        return multiplier
                
                
################ CLASSES      #####################                
                
class Computer():
    
    def __init__(self, pokemon_avail, player):
        
        self.pokemon_avail = pokemon_avail
        self.player = player
        self.pokemon_pool = {}
        
        
    def get_pokemon_pool(self):                
        del self.pokemon_avail[self.player.name]
        
        for pokemon, types in self.pokemon_avail.items():
            self.pokemon_pool[pokemon] = {"types": types, "score": 1}
            
            
    def pokemon_scoring(self):
        pokemon_pool = self.get_pokemon_pool()
        
        for pokemon, data in pokemon_pool.items():
            for types in data["types"]:
                
                data["score"] = _type_iteration(self.player.x2_types, 2, types, data["score"])
                data["score"] = _type_iteration(self.player.half_types, .5, types, data["score"])
                data["score"] = _type_iteration(self.player.immune_types, 0, types, data["score"])
                
        
    def get_comp_pokemon(self, difficulty):
        
        if difficulty == "easy":    
            pokemon = sorted(self.pokemon_pool.items(), key= lambda m: m[1]["score"])[0]

            
        elif difficulty == "medium":
            pokemon = sorted(self.pokemon_pool.items(), key= lambda m: m[1]["score"])
            pokemon = pokemon[len(pokemon)// 2]
            
        
        elif difficulty == "hard":
            pokemon = sorted(self.pokemon_pool.items(), key= lambda m: m[1]["score"], reverse= True)
            pokemon = pokemon[randint(1,2)]
            
        
        elif difficulty == "god":
            pokemon = sorted(self.pokemon_pool.items(), key= lambda m: m[1]["score"], reverse= True)[0]
            
            
        pokemon_name = pokemon[0]
            




class Battle_Mechanincs():
    
    def __init__(self, player, ai):
        
        self.player = player
        self.ai = ai
        

        self.attacker = None
        self.defender = None

        self.battle_over = False
        self.winner = None

        self.move = None
        self.current_turn = None
        
        self.multiplier = 1
        
        
    def turn_selector(self):

        self.attacker = self.player if self.player.speed > self.ai.speed else self.ai


    def type_multiplier(self):
        move_type = self.attacker.moves_dict[self.move]["type"]
        
        self.multiplier = _type_iteration(self.defender.x2_types, self.multiplier, move_type, 2)
        self.multiplier = _type_iteration(self.defender.half_types, self.multiplier, move_type, 0.5)
        self.multiplier = _type_iteration(self.defender.immune_types, self.multiplier, move_type, 0)   
            