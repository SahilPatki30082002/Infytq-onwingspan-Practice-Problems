class Country:
    def __init__(self, population,name) -> None:
        self.is_big = None
        self.population = population
        self.name = name
    def compare_pd(self, other):
        clause = ""
        if other.population > self.population:
            clause = "large" 
        elif other.population< self.population:
            clause = "smaller"
        else:
            clause = "same"
        sentence = f'{other.name} has a {clause} pospulation density as {self.__name}.'
        return sentence
c1 = Country(1, "s")
c2 = Country(2, "a")
c1.compare_pd(c2)