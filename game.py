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

    sisu_method = int(input("1. Sign in\n2.Sign up"))
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
        credential_check("Username", auth_manager.username_verifier(username))

        if pass_allowed:
        
            password = input("Password: ")
            credential_check("Password", auth_manager.pass_verifier(password))

        if passkey_allowed:
                
                passkey = input("Passkey: ")
                credential_check("Passkey", auth_manager.pass_verifier(passkey))

                if newpass_allowed:
                        
                        new_password = input("New Password: ")
                        credential_check("New Password", auth_manager.pass_verifier(new_password))

                        return username, passkey, new_password


                return username, password, passkey, new_password


        return username, password

def signup_menu_draw():
        username, password, passkey = page_credentials_draw(True, True, False)

        auth_manager.add_and_change_credentials(username, password, passkey)
        file_manager.save_user_credentials(credentials)


def signin_menu_draw():
        while True:
            forget_password = input("Forgot Password? (yes or no) ")

            if forget_password: 
                    while True:

                        username, new_password, passkey = page_credentials_draw(False, True, True)
                        result, credentials = auth_manager.forgot_password(username, passkey, new_password)

                        if not result:
                            continue
                        else:
                            forget_password
                            break
        
            else:
                while True:

                    username, password = page_credentials_draw(True, False, False)
                    result = auth_manager.login(username, password)

                    if result:
                        break