import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay
import numpy as np


#initialize array with 20 random points 
points = np.random.randint(20, size=(100,2))
# plt.scatter(points[:,0], points[:,1])
vor = Voronoi(points)
tri = Delaunay(points)
plt.triplot(points[:,0], points[:,1], tri.simplices)        # plot triangles
# plt.plot(points[:,0], points[:,1], 'o')

# fig = voronoi_plot_2d(vor)

plt.plot(points[:,0],points[:,1],'o')                       # plot points
plt.plot(vor.vertices[:,0], vor.vertices[:,1],'*')          # plot vertices
plt.xlim(-3,20)
plt.ylim(-3,20)


for simplex in vor.ridge_vertices:
    simplex = np.asarray(simplex)
    if np.all(simplex >= 0):
        plt.plot(vor.vertices[simplex, 0], vor.vertices[simplex, 1], 'k-')

# ridges extending to infinity 
center = points.mean(axis=0)
for pointidx, simplex in zip(vor.ridge_points, vor.ridge_vertices):
    simplex = np.asarray(simplex)
    if np.any(simplex < 0):
        i = simplex[simplex >= 0][0] # finite end Voronoi vertex
        t = points[pointidx[1]] - points[pointidx[0]]  # tangent
        t = t / np.linalg.norm(t)
        n = np.array([-t[1], t[0]]) # normal
        midpoint = points[pointidx].mean(axis=0)
        far_point = vor.vertices[i] + np.sign(np.dot(midpoint - center, n)) * n * 100
        plt.plot([vor.vertices[i,0], far_point[0]],
                 [vor.vertices[i,1], far_point[1]], 'k--')
plt.show()