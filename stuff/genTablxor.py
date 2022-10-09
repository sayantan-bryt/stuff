for i in range(0, 20):
    for j in range(0,20):
        f,s =  bin(i ^ j).split('0b')
        print(str(i) + " xor " + str(j) + '='+  str(s) + '   ' + str(i^j))
    print()
