#!/usr/bin/env python3

import sys

def convert(number):
    res = ""
    for i in range(len(number)):
        if number[len(number)-1-i] == "1":
            res =  chr(ord("a")+(i%10)) + res
        else:
            res = "0" + res
    return res
    

def my_printf(format_string,param):
    if not format_string:
        print("")
        return
    elif not "#b" in format_string or not param:
        print(format_string)
        return
    
    is_negative = False
    if param[0] == '-':
        param = param[1:]
        is_negative = True
    try:
        number = convert(str(bin(int(param))[2:]))
    except:
        print(format_string)
        return
    
    if is_negative:
        number = "-" + number
        
    print(format_string.replace("#b", number))
    

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
