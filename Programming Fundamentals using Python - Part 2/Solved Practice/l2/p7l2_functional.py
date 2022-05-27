#lex_auth_0127136447430656001216

def creator(digit,one,five,ten):
    sequence = ""
    if digit!=0:
        if digit>0 and digit<4:
            for i in range(digit):
                sequence+=one
        elif digit == 4:
            sequence+= one + five
        elif digit == 5:
            sequence+= five
        elif digit>5 and digit<9:
            sequence+= five
            for i in range(digit - 5):
                sequence+= one
        elif digit == 9:
            sequence+= one + ten
    return sequence

def convert_to_roman(num):
    roman_digit = ""
    str_num = str(num)
    while(len(str_num)!=4):
        str_num = "0" + str_num
    dig_thousands = int(str_num[0])
    dig_hundreds = int(str_num[1])
    dig_tens = int(str_num[2])
    dig_units = int(str_num[3])
    if dig_thousands!=0:
        for i in range(dig_thousands):
            roman_digit+="M"
    roman_digit += creator(dig_hundreds, "C", "D", "M") + creator(dig_tens, "X", "L", "C") + creator(dig_units, "I", "V", "X")
    
    return roman_digit

for num in range(1,5000):    
    print(num," : ",convert_to_roman(num))