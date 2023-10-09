import datetime
import hashlib

from users.professional import Professional
from users.student_personal import StudentPersonal

class Register:  
    def __init__(self):
        self.id_personal_or_student = 0
        self.id_professional = 0
        self.accounts_personal_or_student = {}
        self.accounts_professional = {}
    
    def save_data(self, filename, data):
        with open(filename, 'a') as file:
            file.write(data)
    
    def load_data_accounts_personal_or_student(self):
        with open("user_database/users_personal_or_student.txt", "r") as file:
            for line in file:
                id_user, name, lastname, email, password, account_type, birthdate, country = line.rstrip().split("|")
                self.accounts[email] = {
                    'id': id_user,
                    'name': name,
                    'lastname': lastname,
                    'password': password,
                    'account_type': account_type,
                    'birthdate': birthdate,
                    'country': country
                }
        
    def load_data_user_personal_or_student(self):
        try:
            with open("user_database/users_personal_or_student.txt", 'r') as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].rstrip("\n")
                    self.id_personal_or_student = int(last_line.split("|")[0])
                else:
                    self.id_personal_or_student = 0
                    
        except FileNotFoundError:
            self.id_personal_or_student = 0
            
    def load_data_user_professional(self):
        try:
            with open("user_database/users_professional.txt", 'r') as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].rstrip("\n")
                    self.id_proffesional = int(last_line.split("|")[0])
                else:
                    self.id_proffesional = 0
                    
        except FileNotFoundError:
            self.id_proffesional = 0
    
    def validate_email(self, email, account_type):
        
        if account_type == 1:
            return True
        else:
            validator = email[-7:]

            if  account_type == 2:
                if validator == ".edu.pe":
                    return True
                else:
                    print("You must enter an educational email")   
                    return False
            else:
                if validator == ".com.pe":
                    return True
                else:
                    print("You must enter a business email")
                    return False

    def validate_password(self, password):
        if len(password) >= 8:
            return True
        else :
            print("Password must contain at least 8 characters")
            return False
    
    def validate_account_type(self, account_type):
            if account_type >= 1 and account_type <= 3:
                return True
            else :
                print("The User type is between 1 and 3")
                return False

    def additional_personal_or_student_information(self, name, lastname, email, password, account_type):            
        def validate_year(year):
            if year <= 2008 :
                return True
            else:
                return False
        
        def validate_month(month):
            if month >= 1 and month <= 12:
                return True
            else:
                return False
            
        def validate_day(day, month):
            if  month % 2 == 0:
                if day >= 1 and day <= 30:
                    return True
                else:
                    return False
            else:
                if day >= 1 and day <= 31:
                    return True
                else:
                    return False
        
        country = input("Country: ")
        
        print("\n-- BIRTHDATE --\n")
        while(True):
            year = int(input("Year: "))
            if validate_year(year):
                break
        
        while(True):
            month = int(input("Month: "))
            if validate_month(month):
                break
        
        while(True): 
            day = int(input("Day: "))
            if validate_day(day, month):
                break
            
        birthdate = datetime.date(year, month, day)
        
        self.id_personal_or_student += 1
        
        self.accounts_personal_or_student[email] = {
            'id': self.id_personal_or_student,
            'name': name,
            'lastname': lastname,
            'password': password,
            'account_type': account_type,
            'birthdate': birthdate,
            'country': country
        }
        
        user = StudentPersonal(self.id_personal_or_student, name, lastname, email, password, account_type, birthdate, country)        
        return user    
        
    def additional_professional_information(self, name, lastname, email, password, account_type):
        
        print("\n-- PROFESSIONAL INFORMATION -- \n")
        company = input("Company: ")
        charge = input("Charge: ")     
        
        self.id_professional += 1  
        
        user = Professional(self.id_professional, name, lastname, email, password, account_type, company, charge) 
        return user    
    
    def register_account(self, account_type, user):  
        
        answer = input("CREATE ACCOUNT? [Yes: y / No: n]: ")
        
        if answer == "y":
            if account_type in [1, 2]:
                filename = "user_database/users_personal_or_student.txt"
                data = f"{user.get_id()}|{user.get_name()}|{user.get_lastname()}|{user.get_email()}|{user.get_password()}|{user.get_account_type()}|{user.get_birthdate()}|{user.get_country()}\n"
            else:
                filename = "user_database/users_professional.txt"
                data = f"{user.get_id()}|{user.get_name()}|{user.get_lastname()}|{user.get_email()}|{user.get_password()}|{user.get_account_type()}|{user.get_company()}|{user.get_charge()}\n"
        
            self.save_data(filename, data)
            
            print("You have successfully registered in the application :)")
        else:
            print("The account has not been created :(")
            
    def ask_for_information(self):
        
        print("____ REGISTER ____\n")
        name = input("Name: ")
        lastname = input("Last name: ")
        
        while(True):
            account_type = int(input("User type [1: Personal  2: Student  3: Professional]: "))
            
            if self.validate_account_type(account_type):
                break
           
        
        while(True):
            email = input("Email: ")
            
            if self.validate_email(email, account_type):
                break
            
        while(True):
            password = input("Password: ")
            
            if self.validate_password(password):
                break
        
        if account_type == 1 or account_type == 2:
           user = self.additional_personal_or_student_information(name, lastname, email, hashlib.sha256(password.encode()).hexdigest(), account_type)
        else:
           user = self.additional_professional_information(name, lastname, email, hashlib.sha256(password.encode()).hexdigest(), account_type)
        
        self.register_account(account_type, user)   
        
    def get_accounts(self):
        return self.accounts  
        