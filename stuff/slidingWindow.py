#!/d/Programs/Python/Python37/python
from random import randint
import numpy as np

l = [[randint(0,560) for i in range(560)] for j in range(560)]
l = np.array(l)
windowList = []

for i in range(0,560,20):
    singWind = []
    for j in range(0,560,20):
        singWind.append(l[i:i+20,j:j+20])
    windowList.append(singWind)

windowList = np.array(windowList)
print(windowList.shape)
