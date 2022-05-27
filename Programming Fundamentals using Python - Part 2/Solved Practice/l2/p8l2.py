#lex_auth_0127136518921830401222

def find_target_positions(input_string, target_word):
    target_list=[]
    word_list = input_string.split()
    for i in range(len(word_list)):
        if word_list[i] == target_word:
            target_list.append(i)
    return target_list

def find_inverted_index(input_string):
    target_dict={}
    word_list = input_string.split()
    set_word_list = list(set(word_list))
    for i in set_word_list:
        target_dict[i] = find_target_positions(input_string, i)
    return target_dict

    
input_string="we dont need no education we dont need no thought control no we dont"
result_dict=find_inverted_index(input_string)
print(result_dict)