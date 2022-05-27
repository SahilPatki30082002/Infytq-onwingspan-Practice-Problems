#lex_auth_0127136008767324161169

def close_number(num1,num2,num3):
    count_close = 0
    count_far = 0
    diff = [num1-num2, num1-num3, num2-num3]
    for i in diff:
        if i == 1 or i ==-1 or i == 0:
            count_close += 1
        elif i >= 2 or i <= -2:
            count_far += 1
    if count_close == 1 and count_far == 2:
        return True
    return False
        
    
    
print(close_number(5,4,2))