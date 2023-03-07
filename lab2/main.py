#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                param = param.swapcase()
                print(param,end="")
                shouldDo=False
            elif format_string[idx] == '#' and format_string[idx+1] == '.':
                i = 2
                while(format_string[idx+i].isnumeric()):
                    i+=1
                if i == 2:
                    format_string[idx]
                    print(format_string[idx],end="")
                elif format_string[idx+i] == 'k':
                    number = int(format_string[idx + 2: idx + i])
                    param = param.swapcase()
                    print(param[0:number],end="")
                    idx += (i + 2)
                    shouldDo=False
            else:
                format_string[idx]
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())