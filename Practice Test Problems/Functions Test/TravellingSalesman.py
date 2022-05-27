#finding number of unique paths
def paths(num):
    prod = 1
    for i in range(1, num+1):
        prod*=i
    return prod #factorial of a number
print(paths(1))
print(paths(3))
print(paths(9))
print(paths(4))