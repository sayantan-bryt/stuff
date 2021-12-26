def gcd(x,y):

    if x<y:
        (x,y) = (y,x)
    if x%y==0:
        return y
    else:
        return(gcd(y,x%y))

def g():
    print(gcd(10,-5))
g()
