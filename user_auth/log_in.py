import os
import hashlib
import time
from user_auth.register import Register
from focus_todo.functionalities import Functionalities


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class LogIn:
    def __init__(self):
        self.option = -1
        self.accounts_personal_student = {}
        self.accounts_professional  = {}

    def load_data_accounts_personal_or_student(self, email_user, password_user):
        with open("user_database/users_personal_or_student.txt", "r") as file:
            for line in file:
                id_user, name, lastname, email, password, account_type, birthdate, country = line.rstrip().split("|")
            
                if email == email_user and password == password_user:
                    self.accounts_personal_student[email] = {
                        'id': id_user,
                        'name': name,
                        'lastname': lastname,
                        'password': password,
                        'account_type': account_type,
                        'birthdate': birthdate,
                        'country': country
                    }
                    
                    return self.accounts_personal_student, True
                
        return {}, False
                  
    def load_data_accounts_professional(self, email_user, password_user):
        with open("user_database/users_professional.txt", "r") as file:
            for line in file:
                id_user, name, lastname, email, password, account_type, company, charge = line.rstrip().split("|")
                
                if email == email_user and password == password_user:
                    self.accounts_professional[email] = {
                        'id': id_user,
                        'name': name,
                        'lastname': lastname,
                        'password': password,
                        'account_type': account_type,
                        'company': company,
                        'charge': charge
                    }
                    
                    return self.accounts_professional, True
                
        return {}, False

    def main_menu(self):
        print("\t\tGET STARTED :)")
        print("\t\t______________\n")
        print("\t\t📒 FOCUS TO-DO 📒\n\n")
        print("\t\t1. 👤 Log In")
        print("\t\t2. 👔 Register")
        print("\t\t3. 🚪 Exit\n")
        
        while True:
            self.option = int(input("\t\tOption: "))
            
            if (self.option >= 1 and self.option <= 3):
                break
            else :
                print("Invalid Option :(\n")
      
    def log_in(self):
        register = Register()
        
        while self.option != 0:
            clear_console()
            self.main_menu()
            clear_console()
            
            if self.option == 1:
                
                print("\t\t🏠 LOG IN")
                print("\t\t__________\n\n")
                email = input("\t\t📧 Email: ")
                password = input("\t\t🔐 Password: ")
                
                validator = email[-7:]
                
                if validator == ".com.pe":
                    accounts, flag = self.load_data_accounts_professional(email, hashlib.sha256(password.encode()).hexdigest())
                    if flag:
                        print("\n\n")
                        print(f"\t\t😀 WELCOME, {accounts[email]['name']} {accounts[email]['lastname']} ✅\n")
                        print("\t\t👉 Enjoy organizing your tasks with Focus To-Do ⏩⏩⏩⏩ ✌")
                        time.sleep(5)
                        
                        clear_console()
                        functionalities = Functionalities(accounts, email, 3)
                        functionalities.features_menu()
                        
                        if functionalities.get_option() == 5:
                            print("\n\n\t\tReturning to the main screen ...\n\n")
                            time.sleep(3)
                        
                    else:
                        print("\t\tEmail or Password is incorrect :(")
                        time.sleep(4)
                else:
                    accounts, flag = self.load_data_accounts_personal_or_student(email, hashlib.sha256(password.encode()).hexdigest())
                    if flag:
                        print("\n\n")
                        print(f"\t\t😀 WELCOME, {accounts[email]['name']} {accounts[email]['lastname']} ✅\n")
                        print("\t\t👉 Enjoy organizing your tasks with Focus To-Do ⏩⏩⏩⏩ ✌")
                        time.sleep(5)
                        
                        clear_console()
                        functionalities = Functionalities(accounts, email, 1)
                        functionalities.features_menu()
                        
                        if functionalities.get_option() == 5:
                            print("\n\n\t\tReturning to the main screen ...\n\n")
                            time.sleep(3)
                    else:
                        print("\t\tEmail or Password is incorrect :(")
                        time.sleep(4)
                               
            elif self.option == 2:
                register.load_data_user_personal_or_student()
                register.ask_for_information()
                time.sleep(2)
            else:
                print("\n\n\t\tSee you later, we hope to see you soon :)\n\n")
                time.sleep(2)
                break

   
        

