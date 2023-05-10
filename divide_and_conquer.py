import random
import myfunctions
from grahams_alg import grahamHull

# find upper and down bridge of 2 convex hulls
def merge(a,b):
    numa = len(a) # number of points for convex hull a
    numb = len(b) # number of points for convex hull b

    ai = 0
    bi = 0

    for i in range(1,numa):     #find rightmost point of a
        if a[i][0] > a[ai][0]:
            ai = i

    for i in range(1,numb):     #find leftmost point of b
        if b[i][0] < b[bi][0]:
            bi = i

    # find upper bridge
    upa, upb = ai, bi
    done = 0
    while not done:
        done = 1
        while myfunctions.orientation(a[upa],a[(upa+1) % numa],b[upb]) > 0:
            upa = (upa + 1) % numa
    
    
        while myfunctions.orientation(b[upb],b[(upb-1) % numb],a[upa]) < 0:
            upb = (upb - 1) % numb
            done = 0
        
        
    
    # find lower bridge
    downa, downb = ai, bi
    done = 0
    while not done:
        done = 1
        while (myfunctions.orientation(a[downa],b[downb],b[(downb+1)%numb])) > 0:
            downb = (downb + 1) % numb
        
        while (myfunctions.orientation(b[downb],a[downa],a[(downa-1) % numa])) < 0:
            downa = (downa - 1) % numa
            done = 0
        
        
    #merged_hull contains the final convex hull after merging the two convex hulls
    merged_hull = []
    ind = upa
    merged_hull.append(a[ind])
    while ind != downa:
        ind = (ind+1) % numa
        merged_hull.append(a[ind])
    
    ind = downb
    merged_hull.append(b[ind])
    while ind != upb:
        ind = (ind + 1) % numb
        merged_hull.append(b[ind])
    
    return merged_hull
    




def divide_and_conquer(coordinates):

    if len(coordinates) <= 5:
        return grahamHull(coordinates)

    left = []           # store left points of coordinates
    right = []          # store right points of coordinates

    half = int(len(coordinates)/2)
    for i in range(half):
        left.append(coordinates[i])
    for i in range(half, len(coordinates)):
        right.append(coordinates[i])
    
    #convex hull for the left and right sets
    left_hull = divide_and_conquer(left)
    right_hull = divide_and_conquer(right)

    #merging convex hulls
    return merge(left_hull, right_hull)



def main():
    coordinates = [(random.randint(0,100),random.randint(0,100)) for i in range(80)]
    coordinates.sort(key = lambda x: [x[0],x[1]])

    # print("Sorted points : ",coordinates)
    convex_hull = divide_and_conquer(coordinates)
    print("convex hull points : ", convex_hull)

    myfunctions.print_plot(coordinates,convex_hull)

if __name__ == "__main__":
    main()

# coordinates = []
# coordinates.append((-10,5))
# coordinates.append((-2,-10))
# coordinates.append((1,7))
# coordinates.append((3,4))
# coordinates.append((5,6))
# coordinates.append((9,3))
# coordinates.append((11,8))
# coordinates.append((15,-11))
# coordinates.append((18,-3))
# coordinates.append((24,-8))






