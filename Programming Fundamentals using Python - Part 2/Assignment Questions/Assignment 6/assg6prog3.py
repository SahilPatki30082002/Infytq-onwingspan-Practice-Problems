def find_smallest_number(num):
    k = 0
    c=0
    while(num):
        k+=1
        for i in range(1,k+1):
            if k%i==0:
                c+=1
        if c==num:
            return k
        c=0
num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)