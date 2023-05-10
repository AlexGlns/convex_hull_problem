import random
import myfunctions

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

    print(hull, side)
        

def main():
    coordinates = []
    coordinates.append((-10,5))
    coordinates.append((-2,-10))
    coordinates.append((1,7))
    coordinates.append((3,4))
    coordinates.append((5,6))
    coordinates.append((9,3))
    coordinates.append((11,8))
    coordinates.append((15,-11))
    coordinates.append((18,-3))
    coordinates.append((24,-8))

    min_x = coordinates[0]
    max_x = coordinates[len(coordinates) - 1]

    #above, below = myfunctions.side_from_line(max_x,min_x,coordinates)
    # print(above,below)

    # print(myfunctions.side_from_line(max_x,min_x,max_x))
    
    quickHull(max_x,min_x, coordinates, 1)
    quickHull(max_x,min_x, coordinates, -1)
    print(hull)

if __name__ == "__main__":
    main()