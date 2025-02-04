import numpy as np
arr = np.array([1,2,3])
mat = np.array([[1,2,4],[2,3,6],[4,5,9]])
print(arr)
print(mat)
mat2 = mat+2
print(mat2)
print(mat2.dot(mat))
print(arr.shape)
print(arr.size)
print(mat.dtype)
print(mat2.shape)

mat3 = np.array([[1,2,3,3],[78,4,53,34],[8,7,53,3]])
print(mat3)

print(np.zeros((5,4)))
print(np.ones((2,5))+5)
print(np.linspace(0,100,10))
print(np.linspace(5,500,3))