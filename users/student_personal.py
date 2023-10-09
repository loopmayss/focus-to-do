import datetime
from users.account import Account

class StudentPersonal(Account):
    def __init__(self, id_user, name, lastname, email, password, account_type, birthdate, country):
        super().__init__(id_user, name, lastname, email, password, account_type)
        self.birthdate = birthdate
        self.country =  country
        
    def get_birthdate(self):
        return self.birthdate
    
    def get_country(self):
        return self.country
    
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate
        
    def set_country(self, country):
        self.country = country
        
    def calculate_age(self):
        now = datetime.date.today()
        age = now.year - self.birthdate.year
        return age
    
    def __str__ (self):
        profile = f"PROFILE\n\n{self._name} {self._lastname}\n\nBirthdate\tAge\n{self.birthdate}\t{self.calculate_age}\n\nEmail\t\t\tAccount Type\n{self._email}\t{self._account_type}"
        
        return profile