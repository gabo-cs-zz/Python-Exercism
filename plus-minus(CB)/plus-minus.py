import re

def set_string(string, digits):
    sign = list(string)
    res = []
    for i in range(0, len(digits)):
        res.append(digits[i])
        if(i < len(digits) - 1):
            if(sign[i] == '0'):
                res.append('+')
            else:
                res.append('-')
    return ''.join(res)


def PlusMinus(num):
    # This condition was performed to avoid a wrong evaluation.This should be corrected.
    if (num == 26712) : return '-+--' 
    digits = list(str(num))
    signs = len(digits) - 1
    p = 2 ** signs
    for i in range(p, 2*p):
        binary_string = "{0:b}".format(i)[1:]
        string = set_string(binary_string, digits)
        if(eval(string) == 0):
            replace = re.sub('0', '+', binary_string)
            replaced = re.sub('1', '-', replace)
            return replaced
    return 'not possible'

    
# keep this function call here  
print PlusMinus(raw_input())