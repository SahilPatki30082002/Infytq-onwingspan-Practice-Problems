#lex_auth_0127136332814499841204

def sum_of_elements(num_list,number):
    result_sum = 0
    occ = [i for i,num in enumerate(num_list) if num==number]
    ignore = set()
    all = set(range(len(num_list)))
    for i in range(len(occ)):
        j1 = occ[i]-1
        j2 = occ[i]+1
        if occ[i] == 0:
            j1 = 0
        if occ[i] == len(num_list)-1:
            j2 = len(num_list)-1
        ignore.add(j1)
        ignore.add(occ[i])
        ignore.add(j2)
    accept = all - ignore
    for i in accept:
        result_sum+=num_list[i]
    return result_sum
      
num_list=[1,7,3,4,1,7,10,5]
number=7
print(sum_of_elements(num_list, number))