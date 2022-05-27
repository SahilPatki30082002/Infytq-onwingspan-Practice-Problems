#lex_auth_0127136426924195841210

def check_well_formatted(input_item,list_label):
    if input_item[0] not in list_label:
        return False
    if not isinstance(input_item, list):
        return False
    if len(input_item)<2:
        return False
        
    for i in range(1, len(input_item)):
        if isinstance(input_item[i], list):
            if check_well_formatted(input_item[i], list_label):
                continue
            else:
                return False
        elif isinstance(input_item[i], str):
            continue
        else:
            return False
    return True   


input_list1=['Ant', ['Apple', 'Mango'], ['Orange']]
list_label1=['Ant', 'Apple', 'Orange']
result=check_well_formatted(input_list1,list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")