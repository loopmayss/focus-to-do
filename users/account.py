class Account:
    
    def __init__ (self, id_user, name, lastname, email, password, account_type):
        self.id = id_user
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.account_type = account_type
        
        
    def get_id(self):
        return self.id
        
    def get_name(self):
        return self.name
    
    def  get_lastname(self):
        return self.lastname
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
    
    def get_account_type(self):
        return self.account_type
    

        

    
    