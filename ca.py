import numpy as np
import matplotlib.pyplot as plt

num =110

rowsize = 300
evolution = 300
arr = np.zeros((rowsize, evolution), dtype=np.int8)
curr = np.zeros(rowsize)
curr[rowsize // 2] = 1
arr[0] = curr # start arr
rule = str(bin(num))[2:]

for i in range(len(rule), 8):
    rule = '0' + rule

rules = {}
    
for i in range(len(rule)):
    toAdd = int(rule[i])
    curr = str(bin(7 - i))[2:]
    for i in range(len(curr), 3):
        curr = '0' + curr
    rules[(int(curr[0]), int(curr[1]), int(curr[2]))] = toAdd


def nextEvol(l, curr, r):
    return rules[(l, curr, r)]

for i in range(1, evolution):
    nrow = np.zeros(rowsize)
    nrow[0] = arr[i-1, rowsize-1]
    nrow[rowsize-1] = arr[i-1, rowsize-1]
    for j in range(1, rowsize-1):
        l = arr[i-1, j-1]
        curr = arr[i-1, j]
        r = arr[i-1, j+1]
        nrow[j] = nextEvol(l, curr, r)
    arr[i] = nrow
    

ax = plt.axes()
ax.imshow(arr, cmap='Greys_r')
plt.show()