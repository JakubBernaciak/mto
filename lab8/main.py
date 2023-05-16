#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    if not format_string or not param:
        print(format_string)
        return
    
    beg = 0
    end = 0
    is_found = False

    for i in range(len(format_string)):
        if format_string[i] == '#' and format_string[i+1] == '.':
            beg = i + 2
            end = beg
            for j in range(i+2,len(format_string)):
                if format_string[j].isnumeric():
                    end += 1
                else:
                    break
            if format_string[end] =='j':
                is_found = True
                break
            
    if not is_found:
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
    
    result = format_string[:beg-2] + param + format_string[end+2:]
    
    print(result)
        
data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
