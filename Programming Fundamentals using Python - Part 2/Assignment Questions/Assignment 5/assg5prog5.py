#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    
    avg = sum(list_of_marks)/len(list_of_marks) 
    amt = 0
    for i in list_of_marks:
        if i > avg:
            amt+=1
    p = (amt/len(list_of_marks)) * 100
    return p

def sort_marks():
    return sorted(list_of_marks)

def generate_frequency():
    freq = [0] * 26
    for i in list_of_marks:
        freq[i] += 1
    return freq

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())