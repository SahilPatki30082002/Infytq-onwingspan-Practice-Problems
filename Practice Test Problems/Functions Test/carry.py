#counting the number of carry in a sum of 2 numbers
def Carry(num1, num2):
    s_num1 = str(num1)
    s_num2 = str(num2)
    max_len = max(len(s_num1), len(s_num2))
    n1_dif = max_len - len(s_num1)
    n2_dif = max_len - len(s_num2)
    s_num1 = ("0" * n1_dif) + s_num1
    s_num2 = ("0" * n2_dif) + s_num2
    carry_count = 0
    carry = 0
    for i in reversed(range(max_len)):
        dig_sum = int(s_num1[i]) + int(s_num2[i])
        if carry == 1:
            dig_sum+=1
            carry = 0
        s_dig_sum = str(dig_sum)
        if len(s_dig_sum)>1:
            carry = 1
            carry_count+=1
        dig_sum += carry
    return carry_count
    
print(Carry(1356,44))
print(Carry(671,329))
print(Carry(1111,3333))
print(Carry(36,135))