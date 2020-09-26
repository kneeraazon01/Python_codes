""" !Lists
 !they need to store four type of values in the memory
  !1. size
 !2. reference counts
 !3. object type
 !4. object value
! vs the numpy only  stores one type that means the type is fixed
 ! thats why the numpy is very fast as compared to the lists
 ! no need of type checking
 !  CONTIGUOUS MEMORY
"""
import numpy as np

a = np.array(
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ],
    # ! dtype="int16", if you have small values why use more memory space? go ahead man
)
print(a)


# ! Get the array dimensin

dimension = np.ndim(a)
print(dimension)

# ! Get the shape of the matrix literally bhanda

print(np.shape(a))


# ! get the data type
print(a.dtype)

# !get the size
print(a.size)
print(a.itemsize)
print(
    a.nbytes
)  # == print(a.size*a.itemsize) # the number of bytes are displayed here == 8 ==int64
