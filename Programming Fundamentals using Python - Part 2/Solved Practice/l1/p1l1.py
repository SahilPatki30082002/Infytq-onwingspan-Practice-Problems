#lex_auth_0127135739583692801137

from pickletools import string1


def add_string(str1):
    ending = ""
    if len(str1)>=3:
        ending = str1[-3:]
        if ending == "ing":
            ending = "ly"
        else:
            ending = "ing"
    return str1 + ending

str1="go"
print(add_string(str1))