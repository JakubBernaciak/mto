#!/usr/bin/env python3

import sys

def number_swap(number):
    return chr(ord('a') + int(number))

def fun(number):
    result = ''
    for i in number:
        result += str((int(i)+5)%10)
    return result

def numberinator(param):
    result = ''
    first_word = param.split('.')[0]
    for letter in first_word:
        result += number_swap(letter)
    return result
    

def my_printf(format_string,param):
    if not format_string:
        print("")
        return
    if not param:
        print(format_string)
        return
        
    is_found = False
    number = 0
    beg = 0
    end = 0
    for i in range(len(format_string)):
        if format_string[i] == '#' and format_string [i+1] =='.':
            for j in range(i+2,len(format_string),1):
                if format_string[j].isnumeric():
                    continue
                elif format_string[j] == 'h':
                    beg = i
                    end = j + 1
                    number = int(format_string[i+2:j])
                    is_found = True
                else:
                    break
    if not is_found:
        print(format_string)
        return
    
    
    result = numberinator(param)
    if '.' in param and number != 0:
        result += '.'
        second = fun(param.split('.')[1])
        if number > len(second):
            result += second + (number - len(second)) * '0'
        else:
            for j in range(number):
                result += second[j]
    elif '.' not in param and number != 0:
        result += '.' + number * '0'
    
    print(format_string[:beg] + result + format_string[end:])
        
    
       
data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
