#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    if not param:
        print(format_string)
        return
    
    is_negative = False
    
    if param[0] == "-":
        is_negative = True
        param = param[1:]
    
    if not param.isnumeric():
        print(format_string)
        return
    
    param = str(int(param))
    
    param = int(param[::-1])
    if is_negative:
        param *= -1;
    param = str(param)
    
    print(format_string.replace("#g",param,1))
    

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
