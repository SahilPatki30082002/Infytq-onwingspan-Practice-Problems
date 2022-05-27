def strict_checker(my_list):
    length = len(my_list)
    inc = False
    dec = False
    nei = False
    for i in range(length-1):
        if my_list[i+1] - my_list[i] > 0:
            inc = True
        elif my_list[i+1] - my_list[i] < 0:
            dec = True
        else:
            nei = True
    if nei:
        return "neither"
    elif inc:
        return "increasing"
    elif dec:
        return "decreasing"
print(strict_checker([1,2,1]))
print(strict_checker([1,1,1]))
print(strict_checker([1,1,-1]))
print(strict_checker([1,2,3]))
print(strict_checker([3,2,1]))