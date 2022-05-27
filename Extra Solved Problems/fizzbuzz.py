def fizzbuzz(limit):
    result = [check_fizzbuzz(x) for x in range(1, limit)]
    return result

def list_fizzbuzz(limit):
    result = []
    for num in range(1,limit):
        if num%5 == 0 and num%3 != 0:
            result.append("Buzz")
        elif num%3 == 0 and num%5 != 0:
            result.append("Fizz")
        elif num%5 == 0 and num%3 == 0:
            result.append("FizzBuzz")
        else:
            result.append(str(num))
    return result
def check_fizzbuzz(num):
    result = ""
    if num%5 == 0 and num%3 != 0:
        result = "Buzz"
    elif num%3 == 0 and num%5 != 0:
        result = "Fizz"
    elif num%5 == 0 and num%3 == 0:
        result = "FizzBuzz"
    else:
        result = str(num)
    return result
print(check_fizzbuzz(5))
print(check_fizzbuzz(3))
print(check_fizzbuzz(15))
print(check_fizzbuzz(4))
print(fizzbuzz(20))
print(list_fizzbuzz(20))
