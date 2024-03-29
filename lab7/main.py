#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    if not format_string or "#j" not in format_string or not param:
        print(format_string)
        return
    
    is_negative = False
    if param[0] == '-':
        is_negative = True
        param = param[1:]
    
    if not param.isnumeric():
        print(format_string)
        return
    
    param = str(hex(int(param)))[2:]
    for letter in ["a","b","c","d","e","f"]:
        param = param.replace(letter,chr(ord(letter)+6))
    
    if is_negative:
        param = "-" + param
    
    print(format_string.replace("#j", param))
        
data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
