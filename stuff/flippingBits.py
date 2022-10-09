
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    ans = 0
    b = bin(n).split('0b')[1]
    b = '0'*(32-len(str(b))) + str(b)
    c = 1
    for i in b:
        ans += (1-int(i)) * 2**(32-c)
        c += 1

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
