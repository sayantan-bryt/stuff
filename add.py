a = 5
b = 4

while not b==0:
    carry = a & b
    a = a ^ b
    b = carry << 1
    print(bin(a).replace('0b', ''), bin(b).replace('0b', ''), bin(carry).replace('0b', ''))
    print(a, b, carry)
