#!/usr/bin/env python3

import sys

def number_swap(number)
    return chr(ord('a') + int(number))

def numberinator(param):
    result = ''
    first_word = param.split('.')[0]
    for letter in first_word:
        result += number_swap(letter)
    
    

def my_printf(format_string,param):
    if not format_string:
        print("")
    if not param or not param.isnumeric():
        print(format_string)
        
    is_found = False
    number = 0
    for i in range(len(format_string)):
        if format_string[i] == '#' and format_string [i+1] =='.':
            for j in range(i+2,len(format_string)):
                if format_string[j].isnumeric():
                    continue
                elif format_string[j] == 'h':
                    number = int(format_string[i+2:j-1])
                    is_found == True
                else:
                    break
    if not is_found:
        print(format_string)
    
    
       
       
data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
