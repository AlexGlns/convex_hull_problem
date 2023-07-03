import random
import myfunctions
import time

def grahamHull(coordinates,visuallization=False):

    lup = []
    lup.append(coordinates[0])
    if visuallization: myfunctions.print_plot(coordinates,lup)
    lup.append(coordinates[1])
    if visuallization: myfunctions.print_plot(coordinates,lup)


    for i in range(2, len(coordinates)):
        lup.append(coordinates[i])
        if visuallization: myfunctions.print_plot(coordinates,lup)
        while len(lup) > 2 and myfunctions.orientation(lup[-3],lup[-2],lup[-1]) > 0:
            lup.pop(-2)
            if visuallization: myfunctions.print_plot(coordinates,lup)
        

    ldown = []
    ldown.append(coordinates[-1])
    ldown.append(coordinates[-2])

    for x in range(len(coordinates)-3,-1,-1):
        ldown.append(coordinates[x])
        if visuallization: myfunctions.print_plot(coordinates,lup + ldown)
        while len(ldown) > 2 and myfunctions.orientation(ldown[-3],ldown[-2],ldown[-1]) > 0:
            ldown.pop(-2)
            if visuallization: myfunctions.print_plot(coordinates,lup + ldown)
        

    ldown.pop()
    ldown.pop(0)

    return(lup + ldown)

def main():
    start = time.time()
    coordinates = [(random.uniform(0,100),random.uniform(0,100)) for i in range(80)]
    coordinates.sort(key = lambda x: [x[0],x[1]])

    hull = grahamHull(coordinates)
    print("points of convex hull : " , hull)
    end = time.time()
    print("Elapsed time: ", end-start)
    myfunctions.print_plot(coordinates,hull,True)


if __name__ == "__main__":
    main()