def find_duplicates(list_of_numbers):
    set_list = set(list_of_numbers)
    dup_list = []
    for i in set_list:
        if list_of_numbers.count(i) >= 2:
            dup_list.append(i)
    return dup_list

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)