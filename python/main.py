import numpy as np

# 行列の定義
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 行列の加算
C = A + B

# 行列の減算
D = A - B

# 行列の積
E = np.dot(A, B)

# 行列の転置
F = A.T

print("行列A:\n", A)
print("行列B:\n", B)
print("行列の加算C:\n", C)
print("行列の減算D:\n", D)
print("行列の積E:\n", E)
print("行列Aの転置F:\n", F)