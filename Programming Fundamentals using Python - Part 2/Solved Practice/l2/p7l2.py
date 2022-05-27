#lex_auth_0127136447430656001216

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
    if dig_hundreds!=0:
        if dig_hundreds>0 and dig_hundreds<4:
            for i in range(dig_hundreds):
                roman_digit+="C"
        elif dig_hundreds == 4:
            roman_digit+="CD"
        elif dig_hundreds == 5:
            roman_digit+="D"
        elif dig_hundreds>5 and dig_hundreds<9:
            roman_digit+="D"
            for i in range(dig_hundreds - 5):
                roman_digit+="C"
        elif dig_hundreds == 9:
            roman_digit+="CM"
    if dig_tens!=0:
        if dig_tens>0 and dig_tens<4:
            for i in range(dig_tens):
                roman_digit+="X"
        elif dig_tens == 4:
            roman_digit+="XL"
        elif dig_tens == 5:
            roman_digit+="L"
        elif dig_tens>5 and dig_tens<9:
            roman_digit+="L"
            for i in range(dig_tens - 5):
                roman_digit+="X"
        elif dig_tens == 9:
            roman_digit+="XC"
    if dig_units!=0:
        if dig_units>0 and dig_units<4:
            for i in range(dig_units):
                roman_digit+="I"
        elif dig_units == 4:
            roman_digit+="IV"
        elif dig_units == 5:
            roman_digit+="V"
        elif dig_units>5 and dig_units<9:
            roman_digit+="V"
            for i in range(dig_units - 5):
                roman_digit+="I"
        elif dig_units == 9:
            roman_digit+="IX"
    return roman_digit 

for num in range(1,5000):    
    print(num," : ",convert_to_roman(num))