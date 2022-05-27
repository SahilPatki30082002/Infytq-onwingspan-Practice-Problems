#finding number of unique solutions in a quadratic equation 
def solutions(a,b,c):
    disc = b**2 - (4*a*c)
    num = 0
    if disc>0:
        num = 2
    elif disc==0:
        num = 1
    return num
print(solutions(1,0,-1))
print(solutions(1,0,0))
print(solutions(1,0,1))