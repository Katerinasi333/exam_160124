import numpy as np
n = int(input())
A = [[float(j) for j in input().split()]for i in range (n)]
n = int(input())
B = [[float(j) for j in input().split()]for i in range (n)]
A = np.linalg.inv (A)
C = A.dot(B)
print(C)