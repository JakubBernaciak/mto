#!/usr/bin/env python3

import sys

def fun(param):
    res = ''
    for letter in param:
        res += chr(((ord(letter) - ord('0'))* 9 + 1)%10 + ord('0'))
    return res

def my_printf(format_string,param):
    if not param:
        print(format_string)
        return
    
    is_negative = False
    if param[0] == '-':
        is_negative = True
        param = param[1:]
        
    if not param.isnumeric():
        print(format_string)
        return
    
    res = ''
    beg = -1
    end = -1
    is_found = False
    for i in range(len(format_string)):
        if format_string[i] == '#' and format_string[i+1] =='.':
            for j in range(i+2,len(format_string),1):
                if format_string[j].isnumeric():
                    continue
                elif format_string[j] == 'g':
                    beg = i
                    end = j
                    is_found = True
                    break
                else:
                    break
        if is_found:
            break
    
    if not is_found:
        print(format_string)
        return
    
    m_len = int(format_string[beg+2:end])
    
    if m_len < len(param):
        res = param
    else:
        res = "0" * (m_len - len(param)) + param 
    
    res = fun(res)
    
    if is_negative:
        res = '-' + res
    
    print(format_string[:beg]+res+format_string[end+1:])

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
