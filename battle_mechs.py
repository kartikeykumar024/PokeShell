class Computer():
    
    def __init__(self):
        pass


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
        


    def helper1(self, list, value):
        move_type = self.attacker.moves_dict[self.move]["type"]
        
        for type in list:    
            if type == move_type:
                
                self.multiplier *= value


    def type_multiplier(self):
        
        self.helper1(self.defender.x2_types, 2)
        self.helper1(self.defender.half_types, 0.5)
        self.helper1(self.defender.immune_types, 0)   
            