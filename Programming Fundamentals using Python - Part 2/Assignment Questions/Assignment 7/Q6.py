#lex_auth_01269446157664256093
'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

Write a python program to find and display the number of circular primes less than the given limit.
'''
def check_prime(number):
    for i in range(2,number):
        if number%i == 0:
            return False
    return True 
    #if the number is prime return true, else return false

def rotations(num):
    s_num = str(num)
    l = len(s_num)
    temp = ""
    rotors = [num]
    for i in range(l-1):
        s_num = s_num[1:] + s_num[0]
        rotors.append(int(s_num))
    return rotors
    # It should return the listi of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]

def get_circular_prime_count(limit):
    count = 0
    for i in range(2, limit):
        rotors = rotations(i)
        for j in rotors:
            if not check_prime(j):
                break
        else:
            count+=1
    return count
        
    #It should return the count of circular prime numbers below the given limit.

#Provide different values for limit and test your program
print(get_circular_prime_count(1000))