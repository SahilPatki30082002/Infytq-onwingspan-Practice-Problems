#lex_auth_0127135811649044481146

def find_nine(nums):
    limit = 4 if len(nums) > 4 else len(nums) 
    for i in range(limit):
        if nums[i] == 9:
            return True
    else:
        return False
        
#if 9 in nums[:4]
# return true else false
nums=[1,4]
print(find_nine(nums))