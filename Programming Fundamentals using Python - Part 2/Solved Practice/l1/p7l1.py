#lex_auth_0127135857243832321154

def seed_no(number,ref_no):
    digits = [int(x) for x in str(number)]
    prod1 = 1
    for i in digits:
        prod1 *= i
    total = prod1 * number
    if total == ref_no:
        return True
    else:
        return False
    
number=124
ref_no=738
print(seed_no(number,ref_no))