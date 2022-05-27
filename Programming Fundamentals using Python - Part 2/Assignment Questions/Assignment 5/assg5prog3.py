def check_double(number):
    double = number * 2
    s_num = str(number)
    s_dub = str(double)
    if len(s_num) == len(s_dub):
        if sorted(s_dub) != sorted(s_num):
            return False
        for i in range(len(s_num)):
            if s_num[i] == s_dub[i]:
                return False
        else:
            return True
    else:
        return False

print(check_double(142857))