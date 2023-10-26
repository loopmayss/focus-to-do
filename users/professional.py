from users.account import Account

class Professional(Account):
    def __init__(self, id_user, name, lastname, email, password, account_type, company, charge):
        super().__init__(id_user, name, lastname, email, password, account_type)
        self.company = company
        self.charge = charge
        
    def get_company(self):
        return self.company

    def get_charge(self):
        return self.charge
    
    
    def set_company(self, company):
        self.company = company

    def set_charge(self, charge):
        self.charge = charge
