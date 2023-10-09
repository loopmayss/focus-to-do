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
        self.accounts_personal_student = {}
        self.accounts_professional  = {}

    def load_data_accounts_personal_or_student(self, email_user, password_user):
        flag = False
        
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
                    
                    flag = True
                    file.close()
                    break
        
        return flag
                        
    def load_data_accounts_professional(self):
        with open("user_database/users_professional.txt", "r") as file:
            for line in file:
                id_user, name, lastname, email, password, account_type, company, charge = line.rstrip().split("|")
                
                self.accounts_professional[email] = {
                    'id': id_user,
                    'name': name,
                    'lastname': lastname,
                    'password': password,
                    'account_type': account_type,
                    'company': company,
                    'charge': charge
                }


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
    
    def main_sreen(self):
        
        self.load_data_accounts_professional()
        self.load_data_accounts_personal_or_student()

            
        while self.option != 0:
            clear_console()
            self.menu()
            clear_console()
            
            if self.option == 1:
                
                print("\t\tLOG IN")
                print("\t\t__________\n\n")
                self.email = input("\t\tEmail: ")
                self.password = input("\t\tPassword: ")
                
                validator = self.email[-7:]
                
                if validator == ".com.pe":
                    

                    if self.email in self.accounts_professional and self.accounts_professional[self.email]["password"] == hashlib.sha256(self.password.encode()).hexdigest():
                        print(f"Welcome, {self.accounts_professional[self.email]['name']} {self.accounts_professional[self.email]['lastname']}")
                        time.sleep(3)
                    else :
                        print("\t\tEmail or Password is incorrect :(")
                        time.sleep(3)
                else:
                    if self.load_data_accounts_personal_or_student(self.email, hashlib.sha256(self.password.encode()).hexdigest()):
                        print("Successfully Log In :)")
                        time.sleep(3)
                    else :
                        print("\t\tEmail or Password is incorrect :(")
                        time.sleep(3)
                    
                    # if self.email in self.accounts_personal_student and self.accounts_personal_student[self.email]["password"] == hashlib.sha256(self.password.encode()).hexdigest():
                    #     print(f"\t\tWelcome, {self.accounts_personal_student[self.email]['name']} {self.accounts_personal_student[self.email]['lastname']}")
                    #     time.sleep(3)
                    # else :
                    #     print("\t\tEmail or Password is incorrect :(")
                    #     time.sleep(3)
                        
            elif self.option == 2:
                register = Register()
                register.load_data_user_personal_or_student()
                register.load_data_user_professional()
                
                register.ask_for_information()
                time.sleep(2)
            else:
                print("\t\tSee you later, we hope to see you soon :)")
                time.sleep(2)
                break