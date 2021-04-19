"""
1a. Given two vectors, use the cross product to create a set of three orthonormal vectors.
"""

from compas.geometry import cross_vectors
from compas.geometry import angle_vectors
import math as m

v1 = [1,2,3]
v2 = [4,5,6]

x1 = # Orthonormal vector 1
x2 = # Orthonormal vector 2
x3 = # Orthonormal vector 3

print(x1)
print(x2)
print(x3)

print(m.degrees(angle_vectors(x1, x2)))
print(m.degrees(angle_vectors(x1, x3)))
print(m.degrees(angle_vectors(x2, x3)))