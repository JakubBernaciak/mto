#!/usr/bin/env python3

import sys

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
    for letter in param:
        if letter == '0':
            res = res + '9'
        else:
            res = res + chr((ord(letter) - ord('0'))%10 - 1 + ord('0'))
    
    if is_negative:
        res = '-' + res
    
    print(format_string.replace("#Xg",res,1))
    

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
