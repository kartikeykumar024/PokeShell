
from battle_mechs import Computer, Battle_Mechanincs
from user_data_manager import FileManager, FileMissingError, Stats, FileCorruptedError, AuthManager
from poke_api import PokemonData


file_manager = FileManager()

try:    
    credentials = file_manager.load_user_credentials()
except (FileMissingError, FileCorruptedError):
    credentials = {}


auth_manager = AuthManager(credentials)


try:
    player_stats = file_manager.load_player_stats()
except (FileMissingError, FileCorruptedError):
    player_stats = {}



print("Welcome to the game! This game is A terminal-based Pokémon battle game built in Python.\n"\
"Battle AI opponents using real PokéAPI data, choose from multiple difficulty levels, manage status effects\n"
"and enjoy strategic turn-based combat.")

print("\n Use numbers and common sense to navigate through menus")

def sisu_method_check(): #sisu : Sign in/ Sign up

    sisu_method = int(input("1. Sign up\n2.Sign in\n\n"))
    return sisu_method

     
def credential_check(field, func):

        while True:

            result = func
            
            if not result:
                print(f"Invalid {field}!")
                continue

            break


def page_credentials_draw(pass_allowed, passkey_allowed, newpass_allowed):

        username = input("Username: ").lower().strip()
        credential_check("Username", auth_manager.field_verifier(username))

        if pass_allowed:
        
            password = input("Password: ").lower().strip()
            credential_check("Password", auth_manager.field_verifier(password))

        if passkey_allowed:
                
                passkey = input("Passkey: ").lower().strip()
                credential_check("Passkey", auth_manager.field_verifier(passkey))

                if newpass_allowed:
                        
                        new_password = input("New Password: ").lower().strip()
                        credential_check("New Password", auth_manager.field_verifier(new_password))

                        return username, new_password, passkey


                return username, password, passkey


        return username, password

def signup_menu_draw():
        while True:

            username, password, passkey = page_credentials_draw(True, True, False)
            result = auth_manager.username_verifier(username)

            if result:

                print("login successful")
                stats = Stats(auth_manager.currentuser, player_stats)

                break

            else:
                print("Invalid combination of fields! LOSER!")
                continue

        auth_manager.credentials = auth_manager.add_and_change_credentials(username, password, passkey)
        file_manager.save_user_credentials(credentials)

        auth_manager.currentuser = username



def signin_menu_draw():
        while not auth_manager.currentuser:

            forget_password = input("Forgot Password? (yes or no): ").strip().lower()

            if forget_password == "yes": 
                    while True:

                        username, new_password, passkey = page_credentials_draw(False, True, True)

                        result, auth_manager.credentials = auth_manager.forgot_password(username, passkey, new_password)
                        file_manager.save_user_credentials(credentials)


                        if not result:
                            print("Invalid combination of fields! LOSER!")
                            print("login successful")

                            continue

                        else:
                            stats = Stats(auth_manager.currentuser, player_stats)
                            break

        
            elif forget_password == "no":
                while True:

                    username, password = page_credentials_draw(True, False, False)
                    result = auth_manager.login(username, password)


                    if result:
                        auth_manager.currentuser = username

                        print("login successful")
                        stats = Stats(auth_manager.currentuser, player_stats)

                        break
                    
                    else:
                        print("Invalid combination of fields! LOSER!")

            else:
                continue


while True:
        if not auth_manager.currentuser:
                
                method = sisu_method_check()

                if method == 1:
                    signup_menu_draw()

                elif method == 2:
                    signin_menu_draw()

                else:
                    print("What a loser! Cant even select properly!")

        else:


                menu = int(input("\n\n1. Play\n2. Accounts\n\n"))
            

                if menu == 1:
                    
                    pokemon_avail= {"Charizard": ["Fire", "Flying"],
                                    "Garchomp": ["Dragon", "Ground"],
                                    "Lucario": ["Fighting", "Steel"],
                                    "Gengar": ["Ghost", "Poison"],
                                    "Gyarados": ["Water", "Flying"],
                                    "Metagross": ["Steel", "Psychic"],
                                    "Tyranitar": ["Rock", "Dark"],
                                    "Scizor": ["Bug", "Steel"],
                                    "Greninja": ["Water", "Dark"],
                                    "Mamoswine": ["Ice", "Ground"]
                                    }
                    
                    print(f"The available pokemons are:")

                    for pokemon, data in pokemon_avail.items():
                        print(f"{pokemon}: {data}")
                        
                    user_pokemon = input("Enter the Name of the pokemon ::: ").lower().strip()
                    
                    difficulty = input("Difficulty\n1. Easy\n2. Medium\n3. Hard\n4. God\n").lower().strip()

                    #computer = PokemonData(comp_pokemon)
                    #battle_mechs = Battle_Mechanincs(player, ai)
                    
                    player = PokemonData(user_pokemon)
                    
                    
                    
                    player.get_pokemon_stats()
                    available_moves = player.get_available_moves()

                
                    print("Enter the name of 4 moves, you wanna chose for the fight")
                    selected_moves = {}
                    
                    for i, name in enumerate(available_moves.keys(), start=1):
                        print(f"{name}\n")
                        
                        
                    for name, url in available_moves.items():
                        print(name)
                        yn = input("would you like to add this move to ur set? ").lower().strip()
                        
                        if yn == "yes":
                            selected_moves[name] = url   
                        
                        if len(selected_moves.keys()) == 4:
                            break
                        
                        
                    battle_mech = Battle_Mechanincs(player)

                    


                elif menu == 2:
                    sub_menu = int(input("\n1. Change Password\n2. Stats\n3. Logout")).lower().strip()

                    if sub_menu == 1:
                         
                        while True:
                        
                            username, new_password, passkey = page_credentials_draw(False, True, True)
                        
                            result, auth_manager.credentials = auth_manager.forgot_password(username, passkey, new_password)
                            file_manager.save_user_credentials(credentials)
                        
                        
                            if not result:
                                print("Invalid combination of fields! LOSER!")
                                continue

                            else:
                                break

                    elif sub_menu == 2:

                        if player_stats:
                             
                            for keys, value in player_stats.items():
                                print(f"{keys} : {value}")

                        else:
                            print("WTF DO YOU WANNA SEE WITHOUT PLAYING A SINGLE GAME!!!!!")

                    elif sub_menu == 3:
                        auth_manager.currentuser = None