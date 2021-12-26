#!/d/Programs/Python/Python37/python
import sys

n = int(sys.argv[1])
for num in range(2, n-1):
    ans = []
    for i in range(1, n-1):
        val = num**i % n
        if len(ans) == 0 or val not in ans:
            ans.append(val)
            continue
        else:
            print('doesn\'t have')
            break


