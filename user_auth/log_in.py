import os
import hashlib
import time
from user_auth.register import Register

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

    def menu(self):
        print("\t\tGET STARTED :)")
        print("\t\t______________\n")
        print("\t\tFOCUS TO-DO\n\n")
        print("\t\t[1]: Log In")
        print("\t\t[2]: Register")
        print("\t\t[3]: Exit\n")
        
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
            self.menu()
            clear_console()
            
            if self.option == 1:
                
                print("\t\tLOG IN")
                print("\t\t__________\n\n")
                email = input("\t\tEmail: ")
                password = input("\t\tPassword: ")
                
                validator = email[-7:]
                
                if validator == ".com.pe":
                    accounts, flag = self.load_data_accounts_professional(email, hashlib.sha256(password.encode()).hexdigest())
                    if flag:
                        print("\n\n")
                        print(f"\t\tWELCOME, {accounts[email]['name']} {accounts[email]['lastname']} :)\n")
                        print("\t\tEnjoy organizing your tasks with Focus To-Do ========>")
                        time.sleep(7)
                    else:
                        print("\t\tEmail or Password is incorrect :(")
                        time.sleep(4)
                else:
                    accounts, flag = self.load_data_accounts_personal_or_student(email, hashlib.sha256(password.encode()).hexdigest())
                    if flag:
                        print("\n\n")
                        print(f"\t\tWELCOME, {accounts[email]['name']} {accounts[email]['lastname']} :)\n")
                        print("\t\tEnjoy organizing your tasks with Focus To-Do ========>")
                        time.sleep(7)
                    else:
                        print("\t\tEmail or Password is incorrect :(")
                        time.sleep(4)
                               
            elif self.option == 2:
                register.load_data_user_personal_or_student()
                register.load_data_user_professional()
                register.ask_for_information()
                time.sleep(2)
            else:
                print("\n\n\t\tSee you later, we hope to see you soon :)\n\n")
                time.sleep(2)
                break



