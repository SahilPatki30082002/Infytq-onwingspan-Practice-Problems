class User:
    count = 0
    def __init__(self, name): self.username = name; User.count+=1; self.my_count = User.count
    def user_count(self): return self.my_count
u1 = User("A"); u2 = User("B"); u3 = User("C"); print(u2.user_count())