#lex_auth_0127135945621340161163

def string_both_ends(input_string):
    new_string = ""
    if len(input_string) < 2:
        return -1
    new_string = input_string[:2] + input_string[-2:]
    return new_string
    
input_string="w3w"
print(string_both_ends(input_string))