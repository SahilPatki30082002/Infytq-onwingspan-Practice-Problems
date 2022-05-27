#lex_auth_0127390295941775362719

class Dog:
    dog_breed_dict = {'Labrador Retriever': 5, 'German Shepherd': 12, 'beagle': 10}
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
        breed_price = {'Labrador Retriever': 800, 'German Shepherd': 1230, 'Beagle': 650}
        return breed_price[breed]
    
    def validate_breed(self):
        for i in self.__breed_list:
            if i not in Dog.dog_breed_dict.keys():
                return False
        return True
                
    def validate_quantity(self):
        for i in self.__breed_list:
            if Dog.dog_breed_dict[i] == 0:
                return False
        return True
        
    def generate_dog_id(self, breed):
        id = ""
        Dog.counter+=1
        id = str(breed[0]) + str(Dog.counter)
        return id
    def calculate_total_price(self):
        if not self.validate_breed():
            return -1
        if not self.validate_quantity():
            return -2
        for i in self.__breed_list:
            Dog.dog_breed_dict[i]-=1
            self.__dog_id_list.append(self.generate_dog_id(i))
            self.__price += self.get_dog_price(i)
        if self.__accessories_required:
            self.__price += 350
        if self.__price > 1500:
            self.__price -= 0.05*self.__price