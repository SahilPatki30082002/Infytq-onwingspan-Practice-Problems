#lex_auth_0127390295941775362719

class Dog:
    dog_breed_dict = {}
    counter = 100
    def __init__(self, breed_list, accessories_required):
        self.__dog_id_list = []
        self.__breed_list = breed_list
        self.__accessories_required = accessories_required
        self.__price = 0
    
    def get_dog_id_list(self):
        return self.__dog_id_list
    def get_breed_list(self):
        return self.__breed_list
    def get_accessories_required(self):
        return self.__accessories_required
    def get_price(self):
        return self.__price
    def get_dog_price(self, breed):
        pass
    
    def validate_breed(self):
        pass 
    def validate_quantity(self):
        pass
    def generate_dog_id(self, breed):
        pass
    def calculate_total_price(self):
        pass