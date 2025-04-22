import numpy as np
import pandas as pd

arr = np.array([1,2,3,4,5])
matrix = np.array([[1,3],[4,5]])

print(arr.shape, arr.dtype)
print(matrix.shape,arr.dtype)
print(np.zeros((2,4)),np.ones((4,5)))
print(np.arange(0,50,5))
print(np.linspace(10,100,5))
print(arr-2)
print(arr*7)
print(arr**5*10)
print(np.identity(6))
# print(np.zeros())
print(matrix.mean())
print(matrix.std())
print(matrix.sum())
print(arr.mean())
print(arr.std())
print(arr.sum())