"""
1b. Use the cross product to compute the area of a convex, 2D polygon with more than 3 sides.
"""

from compas.geometry import Vector
from compas.geometry import area_polygon

#Input points
a = #...
b = #...
c = #...
# additional points
polygon = [a,b,c] # add additional points here

ab = #Vector1
ac = #Vector2
# additional vectors

#Calculate area
A = #Area

# Display area
print(A)

# Area as computed by the area_polygon function of compas
A2 = area_polygon(polygon)
print(A2)
#and check your result
print("Area correct:", A == A2)


