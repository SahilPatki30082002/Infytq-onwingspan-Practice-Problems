def divisible_by_left(num):
    my_list = [False]
    ll = str(num)
    for i in range(1, len(ll)):
        if int(ll[i])%int(ll[i-1]) == 0:
            my_list.append("True")
        else:
            my_list.append("False")
    return my_list
print(divisible_by_left(73312))
print(divisible_by_left(635))
print(divisible_by_left(1))