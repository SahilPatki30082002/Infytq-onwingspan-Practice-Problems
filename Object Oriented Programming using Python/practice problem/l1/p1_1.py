#lex_auth_0127390120635678722716

class Purchase:
    list_of_items = ["Cake", "Soap", "Jam", "Cereal", "Hand Sanitizer", "Biscuits", "Bread"]
    list_of_count_of_each_item_sold = [0, 0, 0, 0, 0, 0, 0, 0]
    def __init__(self):
        self.__items_purchased = []
        self.__item_on_offer = None
        
    def provide_offer(self):
        offer_item = 'HAND SANITIZER'
        for i in Purchase.list_of_items:
            if i.lower() == offer_item.lower():
                ind = Purchase.list_of_items.index(i)
                break
        Purchase.list_of_count_of_each_item_sold[ind] += 1
        self.__item_on_offer = offer_item
        
    def get_item_on_offer(self):
        return self.__get_item_on_offer
        
    def get_items_purchased(self):
        return self.__get_items_purchased
        
    def sell_items(self, list_of_items_to_be_purchased):
        for item in list_of_items_to_be_purchased:
            for i in Purchase.list_of_items:
                if item.lower() == i.lower():
                    if item.lower() == "soap":
                        self.provide_offer()
                    index = Purchase.list_of_items.index(i)
                    self.__items_purchased.append(i)
                    Purchase.list_of_count_of_each_item_sold[index] += 1 
                    break
                    
    @staticmethod 
    def find_total_items_sold():
        return sum(Purchase.list_of_count_of_each_item_sold)
        
p1 = Purchase()
Purchase.list_of_items = ['Apple', 'Biscuits', 'Chocolates', 'Jam', 'Butter', 'Milk', 'Soap', 'Hand Sanitizer']
p1.sell_items(['JAM', 'CHOcolates', 'Ghee', 'Soap'])
