""" 
Convex Hull Assignment: COSC262 (2018) 
Student Name: Thomas Knight 
Usercode: tkn14 
""" 
 
from math import sqrt 
 

def readDataPts(filename, N): 
    """Reads the first N lines of data from the input file 
          and returns a list of N tuples 
          [(x0,y0), (x1, y1), ...] 
    """ 
    # Opens input file
    infile = open(filename) 
    
    # Creates ouput list
    listPts = [] 
    
    # Reads N lines from input file
    for line in range(N): 
        
        # Reads one set of coordinates
        line = infile.readline() 
        
        #Formats the coordinate into a tuple and adds it to the ouput list
        data = line.strip('\n').split(' ') 
        listPts.append((float(data[0]), float(data[1]))) 
    
    return listPts 
 

def theta(pointA, pointB): 
    """Computes an approximation of the angle between 
       the line AB and a horizontal line through A. 
    """ 
    dx = pointB[0] - pointA[0] 
    dy = pointB[1] - pointA[1] 
    if abs(dx) < 1.e-6 and abs(dy) < 1.e-6: 
        t = 0 
    else: 
        t = dy/(abs(dx) + abs(dy)) 
    if dx < 0: 
        t = 2 - t 
    elif dy < 0: 
        t = 4 + t 
    return t * 90 


def rightmost_lower(pts):
    """Returns the rightmost lowest point in a list of points"""
    index, x_max, y_min = 0, pts[0][0], pts[0][1] 
    for i, points in enumerate(pts):
        x, y = points[0], points[1]
        if (y < y_min) or (y == y_min and x > x_max):
            index, x_max, y_min = i, x, y
    return index
 

def giftwrap(listPts): 
    """Returns the convex hull vertices computed using the 
          giftwrap algorithm as a list of m tuples 
          [(u0,v0), (u1,v1), ...]     
    """ 
    #Your implementation goes here 
    
    pts = listPts[:] 
 
    # Finds the index of the point with minimum y value that is rightmost
    k = rightmost_lower(pts) 
    
    # Variables initialised for points list index and minimum angle
    i = 0 
    v = 0 
    
    # Adds the starting point to the end of the points list
    pts.append(pts[k])  

    # Iterate over points list while the next point is not the starting point
    while (k != (len(pts) - 1)): 
        
        # Interchange the current point and the point with the smallest angle 
        # with the horizontal line
        pts[i], pts[k] = pts[k], pts[i] 
        
        minAngle = 361 
        
        # Iterates over the unvisited points and finds the point with the
        # smallest angle with the horizontal line also  Deals with case where
        # ambiguous case where angle = 0 degrees but should be 360 degrees
        for j in range(i, len(pts)): 
            angle = theta(pts[i], pts[j]) 
            if angle == 0:
                angle = 360
            if (angle < minAngle and angle > v and pts[j] != pts[i]): 
                minAngle = angle 
                k = j 
        
        # Advances to the next point
        i +=1 
        
        # Stores the current minimum angle
        v = minAngle 
    
    # Returns the points list from the start to index i as that is when the
    # convex hull has been completed by returning to the starting point
    return pts[:i] 
 

def lineFn(ptA, ptB, ptC): 
    return ( 
        (ptB[0] - ptA[0]) * (ptC[1] - ptA[1]) -  
        (ptB[1] - ptA[1]) * (ptC[0] - ptA[0])) 
 

def isCCW(ptA, ptB, ptC): 
    return lineFn(ptA, ptB, ptC) > 0 
 

def grahamscan(listPts): 
    """Returns the convex hull vertices computed using the 
         Graham-scan algorithm as a list of m tuples 
         [(u0,v0), (u1,v1), ...]   
    """ 
    #Your implementation goes here 
    
    pts = listPts[:]  
    
    # Finds point with minimum y value that is rightmost
    start_point = pts[rightmost_lower(pts)] 
    
    # Creates a new list (list_of_points) and sort the points list in ascending
    # order corresponding to the angle they make with the starting point  
    list_of_points = []  
    smallest_angle = lambda angle:theta(start_point, angle) 
    list_of_points = sorted(pts[:], key=smallest_angle) 
    
    # Creates a stack with the first three points of list_of_points
    stack = [list_of_points[0], 
             list_of_points[1], 
             list_of_points[2]] 
    
    # Iterates through list_of_points. If the previous two points make a 
    # counter-clockwise turn with the current point then the current point is 
    # pushed onto the stack otherwise if the previous two points don't make a 
    # counter-clockwise turn with the current point then the last point is
    # popped off the stack
    for i in range(3, len(list_of_points)): 
        while not isCCW(stack[-2], stack[-1], list_of_points[i]): 
            stack.pop() 
        stack.append(list_of_points[i])   
    
    # Returns the stack after iterating through all the points in list_of_points
    # as that is when the convex hull has been completed
    return stack


def amethod(listPts):
    """Returns the convex hull vertices computed using 
       Andrew's monotone chain algorithm
    """
    pts = listPts[:]
    
    # Sorts the points
    pts = sorted(pts)
    
    # Constructs the upper hull
    upper_hull = []
    for pt in reversed(pts):
        while (len(upper_hull) >= 2 and not
               isCCW(upper_hull[-2], upper_hull[-1], pt)):
            upper_hull.pop()
        upper_hull.append(pt)   
      
    # Constructs the lower hull
    lower_hull = []
    for pt in pts:
        while (len(lower_hull) >= 2 and not
               isCCW(lower_hull[-2], lower_hull[-1], pt)):
            lower_hull.pop()
        lower_hull.append(pt)
    
    # Concatenates the upper and lower hulls to give the convex hull.
    # The last point of the upper and lower hulls are excluded because they are 
    # repeated at the beggining of the other hulls
    chull = lower_hull[:-1] + upper_hull[:-1]
    
    # Returns the convex hull
    return chull
     

def main(): 
    listPts = readDataPts('A_30000.dat', 30000)  #File name, numPts given as example only 
    #print(giftwrap(listPts))      #You may replace these three print statements 
    #print (grahamscan(listPts))   #with any code for validating your outputs 
    print (amethod(listPts))      
 
  
if __name__  ==  "__main__": 
    main()