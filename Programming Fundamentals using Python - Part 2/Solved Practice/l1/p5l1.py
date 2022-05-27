def count_digits_letters(sentence):
    result_list = list()
    letter = digit =0
    for i in range(len(sentence)):
        if sentence[i].isalpha():
            letter += 1
        elif sentence[i].isdigit():
            digit +=1
    result_list.append(letter)
    result_list.append(digit)
  
    return result_list

sentence="Infosys 123"
print(count_digits_letters(sentence))