
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theGreatXor function below.
def theGreatXor(x):
    b = bin(x).split('0b')[1]
    a = 0
    c = 1
    for i in b:
        a += (1-int(i)) * 2 ** (len(b)-c)
        c += 1
    print(a)
    return a
    # count = 0
    # for i in range(a):
    #     if a ^ x > x:
    #         count += 1
    # return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        x = int(input())

        result = theGreatXor(x)

        fptr.write(str(result) + '\n')

    fptr.close()
