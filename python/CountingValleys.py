#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    V = 0
    M = 0
    count = 0 
    total_valley = 0
    for i in range(steps):
        if count < 0  and V == 0 :
            #print(f"inside {count}")
            V = 1
        if path[i] == 'U':
            count += 1
        if path[i] == 'D':
            count -=1
        if count ==0 and V == 1 :

            total_valley +=1
            V = 0
        
        #print(count)
    #print(f"total valley is  {total_valley}")
    return total_valley
        

print(countingValleys(12,'DDUUDDUDUUUD'))


