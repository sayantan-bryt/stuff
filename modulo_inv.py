#!/d/Programs/Python/Python37/python

import sys

divisor = 550  # sys.argv[1]
dividend = 1769 # sys.argv[2]

quotient = dividend//divisor
remainder = dividend - divisor*quotient
dp = []
while True:
  dp.append([dividend, divisor, quotient, remainder])
  if quotient != 1:
    print("%d = %d * %d + %d" % (dividend, divisor, quotient, remainder))
  else:
    print("%d = %d + %d" % (dividend, divisor, remainder))
  if remainder == 1:
    break
  dividend = divisor
  divisor = remainder
  quotient = dividend // divisor
  remainder = dividend - divisor*quotient

print()
print('%d = %d - %d x %d' % (remainder, dividend, divisor, quotient))
print()

last = len(dp) - 2
m1, m2 = 0, 0
a, b = 0, 0
while last >= 0:
  a = dp[last+1][0]
  b = '(' + str(dp[last+1][0]) + '-' + str(dp[last+1][1]) + ')' + '*' + str(dp[last+1][2]) 
  print('Substituting %s:' % dp[last][-1])
  print('%s = %s - %s' % (1, a, b))
  last -= 1


