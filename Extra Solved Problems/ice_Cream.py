class Icecream:
    sweetness_value = {
        "Plain":0, 
        "Vanilla":5, 
        "ChocolateChip":5, 
        "Strawberry":10, 
        "Chocolate":10
        }
    def __init__(self, flavour, num_sprinkles) -> None:
        self.flavour=flavour
        self.num_sprinkles=num_sprinkles
def sweetest_icecream(my_list):
    values = []
    for i in my_list:
        values.append(Icecream.sweetness_value[i.flavour] + i.num_sprinkles)
    return max(values)

ice1 = Icecream("ChocolateChip", 12)
ice2 = Icecream("Strawberry", 0)
ice3 = Icecream("Chocolate", 23)
print(sweetest_icecream([ice1, ice2, ice3]))