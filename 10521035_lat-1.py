import numpy as np
n_array = np.array([[0, 1, 2, 3],
 [4, 5, 6, 7],
 [8, 9, 10, 11]])
print (n_array.ndim)
print (n_array.shape)
print (n_array.size)
print (n_array.dtype.name)

a = np.array( [11, 12, 13, 14])
b = np.array( [ 1, 2, 3, 4])
c = a - b
print (c)

print (b**2)

print(np.cos(b))

print(b<2)

A1 = np.array([[1, 1],
 [0, 1]])
A2 = np.array([[2, 0],
 [3, 4]])
print (A1 * A2)
print (np.dot(A1, A2))

print (n_array[0,1])

print (n_array[ 0 , 0:3 ])

print (n_array[ 0 , : ])

print (n_array[ : , 1 ])

print (n_array.ravel())

n_array.shape = (6,2)
print (n_array)
print (n_array.transpose())