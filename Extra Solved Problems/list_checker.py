def checker_maker(my_list):
    length = len(my_list)
    half1 = my_list[:length//2]
    half2 = my_list[length//2:]
    sum1 = sum(half1)
    sum2 = sum(half2)
    if sum1>sum2: return half1 + half1
    if sum1<sum2: return half2 + half2
    else: return half1 + half2
print(checker_maker([0,5,5,6,3,1]))