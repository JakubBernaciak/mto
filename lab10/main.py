#!/usr/bin/env python3

import sys

def fun(number):
    new_number = int(number*2/len(str(number)))
    if new_number%2 == 1:
        return str(hex(new_number)).replace('0x', '')
    return str(new_number)

def my_printf(format_string,param):
    if not format_string:
        print("")
        return
    
    if not param:
        print(format_string)
        return
    
    is_negagtive = False
    if param[0] == '-':
        param = param[1:]
        is_negagtive = True
    if not "#a" in format_string or not param or not param.isnumeric():
        print(format_string)
        return
    if not is_negagtive:
        print(format_string.replace("#a", fun(int(param))))
    else:
        print("-"+format_string.replace("#a", fun(int(param))))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
