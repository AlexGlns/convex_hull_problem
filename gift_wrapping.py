import random
import myfunctions
import time

start = time.time()
coordinates = [(random.randint(0,100),random.randint(0,100)) for i in range(80)]
coordinates.sort(key = lambda x: [x[0],x[1]])
leftmost_point = coordinates[0]
convex_hull = []

current_point = leftmost_point

index = 1
while True:
    convex_hull.append(current_point)
    next_point = coordinates[index]
    
    for point in coordinates:
        o = myfunctions.orientation(current_point,next_point,point)
        if (next_point == current_point or o > 0
            or (o == 0 and myfunctions.dist(current_point, point) > myfunctions.dist(current_point, next_point))):
            next_point = point
    
    current_point = next_point
    index+=1
    if current_point == leftmost_point:
        break;

print("convex hull points : ",convex_hull)
end = time.time()
print("Elapsed time: ", end-start)
myfunctions.print_plot(coordinates,convex_hull,True)



