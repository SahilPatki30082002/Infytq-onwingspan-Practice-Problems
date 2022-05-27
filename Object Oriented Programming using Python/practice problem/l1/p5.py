#lex_auth_012752531983671296301
#Start writing you code here
import time
from time import strftime as t
from datetime import date, timedelta
class GarmentOrder:
    garment_dict = {"shirt":[45,400,30],"trousers":[250,500,25],"saree":[500,750,10],"jersey": [750,200,5]}
    def __init__(self, cloth_type, no_of_piece):
        self.__cloth_type = cloth_type
        self.__no_of_piece = no_of_piece
        self.__order_date = time.strftime("%d/%m/%Y")
        self.__delivery_date = None
    
    def get_cloth_type(self):
        return self.__cloth_type
    def get_no_of_piece(self):
        return self.__no_of_piece
    def get_order_date(self):
        return self.__order_date
    def get_delivery_date(self):
        return self.__delivery_date
        
    def calculate_amount(self):
        total = 0
        total += GarmentOrder.garment_dict[self.get_cloth_type()][1] * self.get_no_of_piece()
        return total
        
    def update_stock(self):
        d = date.today() + timedelta(days = GarmentOrder.garment_dict[self.get_cloth_type()][2])
        self.__delivery_date = d.strftime("%d/%m/%Y")
        GarmentOrder.garment_dict[self.get_cloth_type()][0] -= self.get_no_of_piece()
        
    def take_order(self):
        # self.__cloth_type = self.get_cloth_type().lower(
        if self.get_cloth_type() not in GarmentOrder.garment_dict.keys():
            return -1
        if GarmentOrder.garment_dict[self.get_cloth_type()][0] < self.get_no_of_piece():
            return -1
        self.update_stock()
        return self.calculate_amount()
    
g = GarmentOrder('SAREE', 15)
GarmentOrder.garment_dict={'trousers': [40, 600, 30], 'jersey': [15, 500, 10], 'shirt': [70, 800, 40], 'saree': [25, 1000, 20]}
g.take_order()