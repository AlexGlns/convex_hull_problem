import random
import myfunctions
import time

hull = set()

def quickHull(a,b,coordinates, side):
    n = len(coordinates)
    ind = -1
    max_dist = 0
    for i in range(n):
        temp = myfunctions.distance_from_line(a,b,coordinates[i])
        if (myfunctions.side_from_line(a,b,coordinates[i]) == side) and (temp > max_dist):
            ind = i
            max_dist = temp
    
    if (ind == -1):
        hull.add(a)
        hull.add(b)
        return
    
    quickHull(coordinates[ind],a,coordinates,-myfunctions.side_from_line(coordinates[ind],a,b))
    quickHull(coordinates[ind],b,coordinates,-myfunctions.side_from_line(coordinates[ind],b,a))

        

def main():
    start = time.time()
    coordinates = []
    coordinates = [(random.uniform(0,100),random.uniform(0,100)) for i in range(80)]
    coordinates.sort(key = lambda x: [x[0],x[1]])
    min_x = coordinates[0]
    max_x = coordinates[len(coordinates) - 1]
 
    quickHull(max_x,min_x, coordinates, 1)
    quickHull(max_x,min_x, coordinates, -1)
    print("Convex Hull points :",hull)
    end = time.time()
    print("Elapsed time: ", end-start)

if __name__ == "__main__":
    main()