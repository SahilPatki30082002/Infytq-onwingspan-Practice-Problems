#lex_auth_0127390120635678722716
#Start writing you code here
class Purchase:
    
    def __init__(self):
        self.list_of_items = ["Cake", "Soap", "Jam", "Cereal", "Hand Sanitizer", "Biscuits", "Bread"]
        # self.list_of_items = []
        self.list_of_count_of_each_item_sold = [0, 0, 0, 0, 0, 0, 0, 0]
        self.__items_purchased = []
        self.__item_on_offer = None
        
    def provide_offer(self):
        self.list_of_count_of_each_item_sold[4] = 1
        self.__item_on_offer = "HAND SANITIZER"
        self.__items_purchased.append(self.__item_on_offer)
        
    def get_item_on_offer(self):
        return self.__get_item_on_offer
        
    def get_items_purchased(self):
        return self.__get_items_purchased
        
    def sell_items(self, list_of_items_to_be_purchased):
        for i in range(len(self.list_of_items)):
            if self.list_of_items[i] in list_of_items_to_be_purchased:
                self.list_of_count_of_each_item_sold[i] = 1
                self.__items_purchased.append(self.list_of_items[i])
                if self.list_of_items[i] == "Soap":
                    self.provide_offer()
        
    def find_total_items_sold(self):
        return sum(self.list_of_count_of_each_item_sold)
        
p1 = Purchase()
p1.list_of_items = ['Apple', 'Biscuits', 'Chocolates', 'Jam', 'Butter', 'Milk', 'Soap', 'Hand Sanitizer']
p1.sell_items(['JAM', 'CHOcolates', 'Ghee', 'Soap'])
