from geometer import *
import numpy as np


# Collections of points and lines
coordinates = np.random.randint(100, size=(1000, 2))
points = PointCollection([Point(x, y) for x, y in coordinates])
lines = points.join(-points)
# True

# Ellipses/Quadratic forms
a = Point(-3, 0)
b = Point(3, 0)
c = Point(1, 2)
d = Point(2, 1)
e = Point(0, -1)

conic = Conic.from_points(a, b, c, d, e)
ellipse = Conic.from_foci(c, d, bound=b)

# Geometric shapes
o = Point(0, 0)
x, y = Point(1, 0), Point(0, 1)
r = Rectangle(o, x, x+y, y)
r.area
# 1
