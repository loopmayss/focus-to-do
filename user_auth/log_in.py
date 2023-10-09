import os
import hashlib
import time
from user_auth.register import Register

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class LogIn:
    def __init__(self):
        self.email = ""
        self.password = ""
        self.option = -1
        self.accounts = {}

    def menu(self):
        print("\t\tGET STARTED :)")
        print("\t\t_______________")
        print("\t\tFOCUS TO-DO\n\n")
        print("\t\t[1]: Log In")
        print("\t\t[2]: Register")
        print("\t\t[3]: Exit\n")
        
        while True:
            option = int(input("\t\tOption:"))
            
            if (option >= 1 and option <= 3):
                break
            else :
                print("Invalid Option :(\n")
    
    def log_in(self):
        while self.option != 0:
            clear_console()
            self.menu()
            clear_console()
            
            register = Register()
            
            if self.option == 1:
                register.load_data_accounts()
                self.accounts = register.get_accounts()
                
                print("\t\tLOG IN")
                print("\t\t__________\n\n")
                email = input("Email:")
                password = input("Password:")
                
                if email in self.accounts and self.accounts[email] == hashlib.sha256(password.encode()).hexdigest():
                    print("")
                
            elif self.option == 2:
                register.load_data_user_personal_or_student()
                register.load_data_user_professional()
                register.ask_for_information()
                time.sleep(2)
            else:
                print("See you later, we hope to see you soon :)")
                time.sleep(2)