#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    if len(format_string) == 0:
        print("")
        return
    
    is_found = False
    for i in range(len(format_string)):
        if format_string[i] == '#':
            for j in range(i+1,len(format_string)):
                if format_string[j].isnumeric() or format_string[j] in ['.','k']:
                    if format_string[j] == 'k':
                        beg_i = i
                        end_i = j
                        is_found = True
                        break
                else: break
        if is_found: break
    
    if not is_found:
        print(format_string)
        return
    param = param.swapcase()
    
    dot_i = format_string[beg_i:end_i].find('.')
    if dot_i != -1:
        new_len = int(format_string[beg_i + dot_i +1:end_i])
        param = param[:new_len]
    else: dot_i = end_i - beg_i

    if beg_i + 1 < beg_i + dot_i:
        new_len = int(format_string[beg_i + 1: beg_i + dot_i])
        param = ' ' * (new_len - len(param)) + param
    print(format_string[:beg_i] + param + format_string[end_i + 1:])


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
