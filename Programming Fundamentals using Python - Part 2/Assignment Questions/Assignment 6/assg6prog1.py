def pal(ch1,ch2, word, l):
    if ch1.lower()!=ch2.lower():
        return False
    if l == len(word)//2 - 1:
        return True
    l+=1
    return pal(word[l], word[len(word)-1-l], word, l)
def is_palindrome(word):
    if word == "":
        return True
    return pal(word[0],word[len(word)-1],word, 0)

#Provide different values for word and test your program
result=is_palindrome("MadAM")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")