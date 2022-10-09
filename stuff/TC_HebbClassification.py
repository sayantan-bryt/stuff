def tc_classifier(t, c):
    xt = [[1, 1, 1], [-1, 1, -1], [-1, 1, -1]]
    xc = [[1, 1, 1], [1, -1, -1], [1, 1, 1]]
    bias = 0
    weights = [[0 for j in range(3)] for i in range(3)]
    yt = 1
    yc = -1
    # training
    for test in range(2):
        for i in range(len(xt)):
            for j in range(len(xt[0])):
                if test == 0:
                    weights[i][j] = weights[i][j] + yt * xt[i][j]
                else:
                    weights[i][j] = weights[i][j] + yc * xc[i][j]
        bias = bias + 1

    weights.append(bias)

    # testing
    for test in range(2):
        verify = 0
        for i in range(len(xt)):
            for j in range(len(xt[0])):
                if test == 0:
                    verify = verify + weights[i][j] * t[i][j]
                else:
                    verify = verify + weights[i][j] * c[i][j]
        if verify + weights[i+1] > 0:
            print("Entered matrix is T")
        elif verify + weights[i+1] < 0:
            print("Entered matrix is C")
        else:
            print('Not recognised')


t = [[1, 1, 1], [-1, 1, -1], [-1, 1, -1]]
c = [[1, 1, 1], [1, -1, -1], [1, 1, 1]]

print("Matrix 1: ",  t)
print("Matrix 2: ",  c)

tc_classifier(t, c)
