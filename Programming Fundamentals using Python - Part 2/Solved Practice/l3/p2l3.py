#lex_auth_0127136216235950081185

def ducci_sequence(test_list,n):
    
    
    final_list = []
    prev_ducci = test_list
    for i in range(n+1):
        ducci = []
        for a in range(len(test_list)):
            b = 0
            if a==len(test_list)-1:
                b = 0
            else:
                b = a+1
            ducci.append(abs(prev_ducci[a] - prev_ducci[b]))
        prev_ducci = ducci
        final_list.append(ducci)
    
    return final_list[n]

ducci_element=ducci_sequence([0, 653, 1854, 4063] , 3)
print(ducci_element)