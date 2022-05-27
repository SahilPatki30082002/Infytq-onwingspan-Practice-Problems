#lex_auth_0127135773590405121141

def bracket_pattern(input_str):
    open = 0 
    close = 0 
    op = True
    for i in input_str:
        if i == "(":
            open += 1
        else:
            close += 1
    if open != close:
        return False
    if input_str[0] == ")" or input_str[len(input_str)-1] == "(":
        return False
    return True

    
input_str="(())("
print(bracket_pattern(input_str))