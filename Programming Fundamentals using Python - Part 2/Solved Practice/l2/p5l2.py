#lex_auth_0127136373866577921209

def two_dig(str_num,singles,tens,teens):
    num = int(str_num)
    word = ""
    dig_tens = int(str_num[2])
    dig_units = int(str_num[3])
    rem = num%100
    if rem>10 and rem<20:
        return teens[dig_units-1]
    
    if dig_tens == 0:
        word = singles[dig_units]
    else:
        word = tens[dig_tens] +" "+ singles[dig_units]
    return word
        
        

def integer_to_english(number):
    if number>1000 or number < 1:
        return -1
    singles = ["", "one", "two", "three","four", "five", "six", "seven", "eight", "nine"]
    tens = ['', 'ten', 'twenty', 'thirty', 'fourty','fifty','sixty', 'seventy', 'eighty', 'ninty']
    teens = ['eleven', 'twelve', 'thirteen','fourteen','fifteen', 'sixteen','seventeen','eighteen', 'nineteen']
    english = ""
    str_num =  str(number)
    while(len(str_num)!=4):
        str_num = "0" + str_num
    dig_thousands = int(str_num[0])
    dig_hundreds = int(str_num[1])
    dig_tens = int(str_num[2])
    dig_units = int(str_num[3])
    if dig_thousands!=0:
        english = singles[dig_thousands] + " thousand"
    if dig_hundreds != 0:
        if dig_thousands!=0:
            english+=" "
        english += singles[dig_hundreds] + " hundred"
    if dig_tens!=0 or dig_units!=0:
        if dig_hundreds != 0 or dig_thousands!=0:
            english += ' and '
        english += two_dig(str_num,singles,tens,teens)
    return english


number=212
print(integer_to_english(number))