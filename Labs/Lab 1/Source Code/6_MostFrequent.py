#NumPy create random vector of size 15 having only Integers in the range 0-20.
# Write a program to find the most frequent item/value in the vector list


from random import randint
import numpy as np
Z = np.random.randint(0,25, size=(15))
print("Array: %s"   %Z)
print("Frequent item in the list:")
print(np.bincount(Z).argmax())