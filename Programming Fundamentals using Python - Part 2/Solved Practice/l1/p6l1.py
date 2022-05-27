#lex_auth_0127135869481369601150

def list123(nums):
    limit = 0
    length = len(nums)
    if length < 3:
        return False
    else:
        limit = length - 3 
    for i in range(limit+1):
        if nums[i] == 1:
            if nums[i+1] == 2:
                if nums[i+2] == 3:
                    return True
    else:
        return False
    
    

nums=[1, 2, 1, 2, 1]
print(list123(nums))