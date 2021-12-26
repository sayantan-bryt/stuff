X = [1,2,3,4]
m = 64
a = 13
for x in X:
    c = 0
    l = [x]
    while (x*a)%m not in l:
        x = (x*a)%m
        l.append(x)
        c = c + 1
    print(c+1)
