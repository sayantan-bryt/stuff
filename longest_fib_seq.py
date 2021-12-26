#n = input()
#l = [input() for i in range(n)]
l = [4, 2, 7, 5, 3, 8, 10, 11, 19]

max_elem = max(l)
num = 0
a = 0
b = 1

while num <= max_elem:
    num = a + b
    a = b
    b = num
    print (num , end= ' ')

print()
