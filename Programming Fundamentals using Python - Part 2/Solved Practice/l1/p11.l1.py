#lex_auth_0127136021907046401165

def find_upper_and_lower(sentence):
    low = upper = 0
    result_list = []
    for i in list(sentence):
        if i.isalpha():
            if i.islower():
                low += 1
            if i.isupper():
                upper += 1
    result_list.append(upper)
    result_list.append(low)
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))