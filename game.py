from user_data_manager import FileManager, FileMissingError, Stats, FileCorruptedError, AuthManager


file_manager = FileManager()

try:
    players_stats = file_manager.load_player_stats()
except (FileMissingError, FileCorruptedError):
    stats = {}


try:    
    credentials = file_manager.load_user_credentials()
except (FileMissingError, FileCorruptedError):
    credentials = {}


auth_manager = AuthManager(credentials)


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

        username = input("Username: ")
        credential_check("Username", auth_manager.field_verifier(username))

        if pass_allowed:
        
            password = input("Password: ")
            credential_check("Password", auth_manager.field_verifier(password))

        if passkey_allowed:
                
                passkey = input("Passkey: ")
                credential_check("Passkey", auth_manager.field_verifier(passkey))

                if newpass_allowed:
                        
                        new_password = input("New Password: ")
                        credential_check("New Password", auth_manager.field_verifier(new_password))

                        return username, new_password, passkey


                return username, password, passkey


        return username, password

def signup_menu_draw():
        username, password, passkey = page_credentials_draw(True, True, False)
        while True:
            result = auth_manager.username_verifier(username)

            if result:
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
                            continue
                        else:
                            break
        
            elif forget_password == "no":
                while True:

                    username, password = page_credentials_draw(True, False, False)
                    result = auth_manager.login(username, password)


                    if result:
                        auth_manager.currentuser = username
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
                print("login successful")

