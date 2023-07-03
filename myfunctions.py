import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def orientation(p1,p2,p3):
    return (((p2[0]-p1[0])*(p3[1]-p1[1])) - ((p2[1]-p1[1]) * (p3[0]-p1[0])))

def dist(p1, p2):
    return math.sqrt((p2[1]-p1[1])**2 + (p2[0] - p1[0])**2)

#returns distance between point "point" and the line joining points 'a' and 'b'
def distance_from_line(a,b,point):
    # using formula y = ax + b => ax -y + b = 0
    #find straight line of points a, b
    l = (b[1] - a[1]) / (b[0] - a[0]) # l == a
    c = a[1] - l * a[0]               # c == b

    return abs(l * point[0] -1 * point[1] + c) / math.sqrt(l**2 + (-1)**2)

def side_from_line(p1,p2, p):    
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
 
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

# show all coordinates and draws convex hull with those coordinates 
def print_plot(coordinates,hull,final = False):
    x =[]
    y = []
    
    for i in range(len(coordinates)):
        plt.plot(coordinates[i][0],coordinates[i][1],
                 marker = 'o', markerfacecolor = 'blue',markersize = 8)
        
    
    for i in range(len(hull)):
        x.append(hull[i][0])
        y.append(hull[i][1])

    if final:
        x.append(hull[0][0])
        y.append(hull[0][1])
    plt.plot(x,y,color='red',marker='o',markerfacecolor='red')

    # setting x and y axis range
    plt.ylim(-5,110)
    plt.xlim(-5,110)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    plt.show()