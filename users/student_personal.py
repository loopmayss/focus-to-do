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
        
