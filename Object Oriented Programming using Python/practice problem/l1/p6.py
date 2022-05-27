#lex_auth_012752542731378688302
#Start writing you code here

class Laptop:
    def __init__(self, grcode, expiry):
        self.__grcode = grcode
        self.__expiry = expiry
    
    def get_expiry(self):
        return self.__expiry
    def get_grcode(self):
        return self.__grcode

class Scanner:
    def __init__(self, emp_laptop_dict):
        self.__emp_laptop_dict = emp_laptop_dict
        #{emp_id: lap.qr, ....}
        
    def scan(self, empid, laptop):
        if empid not in self.__emp_laptop_dict.keys():
            return False
        if not laptop.get_expiry():
            return True
        return False