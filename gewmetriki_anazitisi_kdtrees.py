import random

class area:
    def __init__(self,xmin,xmax,ymin,ymax):
        self.xmin=xmin
        self.xmax=xmax
        self.ymin=ymin
        self.ymax=ymax
        
class kd_Node:
    def __init__(self, point):
        self.point = point
        self.left= None
        self.right = None


def fully_contained(node,area):
    if node:
        if area.xmin <= node.point[0] and area.xmax >= node.point[0] and area.ymin <= node.point[1] and area.ymax >= node.point[1]:
            return True
    
    return False

def intersects(node,area):
    if node:
        if area.xmin > node.point[0] and area.xmax < node.point[0] and area.ymin > node.point[1] and area.ymax < node.point[1]:
            return False
    
    return True

def insert(root, point, depth):
    #if tree is empty
    if not root:
        return kd_Node(point)

    # find in which dimension will be the comparison
    dim= depth % 2 # depth mod 2 to find if the comparison is between x or y

    if point[dim] <= root.point[dim]:
        root.left = insert(root.left, point, depth+1)
    else:
        root.right = insert(root.right, point, depth+1)
    
    return root

def range_search(root,area):
    # return a list with the points that are inside area
    result= []
    
    if root == None:
        return result
    
    #check if is leaf
    if root.left == None and root.right == None:
        if area.xmin <= root.point[0] and area.xmax >= root.point[0] and area.ymin <= root.point[1] and area.ymax >= root.point[1]:
            result.append(root.point)

    else:
        if area.xmin <= root.point[0] and area.xmax >= root.point[0] and area.ymin <= root.point[1] and area.ymax >= root.point[1]:
            result.append(root.point)

        if fully_contained(root.left, area):
            result+=traverse(root.left)
        elif intersects(root.left,area):
            result+=range_search(root.left,area)
        
        if fully_contained(root.right, area):
            result+=traverse(root.right)
        elif intersects(root.right,area):
            result+=range_search(root.right,area)

    return result

def traverse(node):
    members = []
    if node:
        members += traverse(node.left)
        members.append(node.point)
        members += traverse(node.right)
    return members

# main program
if __name__ == '__main__':
    root = None

    points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]
    # points =[(random.randint(1,100),random.randint(0,100)) for i in range(60)]
    print("points : ",points)
    area_=area(2,6,0,14)
    for i in range(len(points)):
        root = insert(root,points[i],0)
    print("area : xmin=" , area_.xmin , " xmax=" , area_.xmax , "ymin=" , area_.ymin , " ymax=" , area_.ymax)
    print(range_search(root,area_))
