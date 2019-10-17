import re

def add_string(s):
    '''
    :param s: String Input to be parsed and evaluated by the calculator
    :return: Sum of the string input
    Calculate sum of the strings if only integer value is less than or equal to 1000
    Raise Exception when negative integers are found in the string
    '''
    if s=="":
        return 0
    lis=format_string(s).split('+')
    sum,neg_list=0,[]
    for i in lis:
        try:
            n=int(i)
        except ValueError:
            raise Exception("Invalid Literal Passed")
        if n > 0 and n <= 1000:
            sum += n
        elif n < 0:
            neg_list.append(i)
        else:
            continue
    '''
    Raise Exception with the list of all negative integers present in the string
    '''
    if neg_list:
        error_msg = "Negatives not allowed. Negative number in the expression are " + ",".join(neg_list)
        raise ValueError(error_msg)
    return sum


def format_string(s):
    '''
    :param s: Input string to be parsed
    :return: a list of strings after replacing all delimiters with the addition operator
    Check if the String starts with delimiter, if any delimiter present pasre them and replace with addition operator
    Else replace \n and , with addition operator
    '''
    if re.match(r'^//+',s):
        delimit,str_eval=re.split(r'\n',s,1)
        d=r''+'['+delimit[1:]+']+'
        return re.sub(d,'+',str_eval)
    else:
        return(re.sub('[,\n]+','+',s))
