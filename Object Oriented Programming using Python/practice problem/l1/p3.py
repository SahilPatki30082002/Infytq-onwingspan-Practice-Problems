#lex_auth_01274096553236070462
#Start writing you code here
class Tollbooth:
    
    def __init__(self):
        self.__no_of_vehicle = 0
        self.__total_amount = 0
        
    def calculate_amount(self, vehicle_type):
        toll_details = {'car':70, 'bus': 100, 'truck': 150, 'other': 70}
        if vehicle_type.lower() in toll_details.keys():
            self.__total_amount += toll_details[vehicle_type.lower()]
        else:
            self.__total_amount += toll_details["other"]
        
    def count_vehicle(self):
        self.__no_of_vehicle += 1
        
    def collect_toll(self, owner_type, vehicle_type):
        if owner_type.lower() == "vip":
            self.count_vehicle()
        else:
            self.count_vehicle()
            self.calculate_amount(vehicle_type)
            
    def get_no_of_vehicle(self):
        return self.__no_of_vehicle
    def get_total_amount(self):
        return self.__total_amount