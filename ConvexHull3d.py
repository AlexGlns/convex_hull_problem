import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull

#initialize array with 50 random points 
points = np.random.randint(1,100,(50,3))

hull = ConvexHull(points)   #call ConvexHull to compute 3d hull

plot = plt.figure()         #plot figure
ax = plot.add_subplot(111, projection="3d")
ax.plot(points.T[0],points.T[1],points.T[2],"ko")

for p in hull.simplices:
    p = np.append(p,p[0])
    ax.plot(points[p,0],points[p,1],points[p,2],"r-")


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_xlim3d(-5,105)
ax.set_ylim3d(-5,105)
ax.set_zlim3d(-5,105)

plt.show()
