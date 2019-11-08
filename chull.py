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
    infile = open(filename)
    listPts = []
    for line in range(N):
        line = infile.readline()
        data = line.strip('\n').split(' ')
        listPts.append((float(data[0]), float(data[1])))
    #print(listPts)
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

def giftwrap(listPts):
    """Returns the convex hull vertices computed using the
          giftwrap algorithm as a list of m tuples
          [(u0,v0), (u1,v1), ...]    
    """
    #Your implementation goes here
    pts = listPts[:]
    k = pts.index(min(pts, key = lambda t: t[1]))#Add rightmost lower point part
    i = 0
    v = 0
    pts.append(pts[k]) 
    while (k != (len(pts) - 1)):
        pts[i], pts[k] = pts[k], pts[i]
        minAngle = 361
        for j in range(i, len(pts)):
            angle = theta(pts[i], pts[j])
            if (angle < minAngle and angle > v and pts[j] != pts[i]):
                minAngle = angle
                k = j
        i +=1
        v = minAngle
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
    start_point = min(pts, key = lambda t: t[1]) #Add rightmost lower point part 
    list_of_points = [] 
    smallest_angle = lambda angle:theta(start_point, angle)
    list_of_points = sorted(pts[:], key=smallest_angle)
    stack = [list_of_points[0],
             list_of_points[1],
             list_of_points[2]]
    for i in range(3, len(list_of_points)):
        while not isCCW(stack[-2], stack[-1], list_of_points[i]):
            stack.pop()
        stack.append(list_of_points[i])
    #for point in pts[1:]: 
        #list_of_points.append(theta(start_point, point)) 
    #list_of_points = sorted(list_of_points) 
    #return  chull 
    #return list_of_points  
    return stack

def split_points(r, q, test_pt, pts):
    if len(pts) == 0:
	#return None
	pass

def amethod(listPts):
    """Returns the convex hull vertices computed using 
          a third algorithm
    """
    #Your implementation goes here    
    maxY = -1
    minY = float('inf')
    for p in listPts:
	if p[1] > maxY:
            maxY = p[1]
            q = p
        if p[1] < minY:
            minY = p[1]
            r = p
    listPts.remove(r)
    listPts.remove(q)
    chull = r + q
    [set0, set1] = split_points(r, q, q, listPts)
    quick_hull(set0, r, q)
    quick_hull(set1, r, q)
    
##def quick_hull(pts, r, q):
    ##furthest_pt = []
    ##max_dist = -1
    ##if pts == []:
	##return None 
    ##if len(pts) == 1:
	##furthest_pt = pts
    ##for p in pts:
	##temp = sqrt((r[0] - p[0]) ** 2 + (r[1] - p[1]) ** 2) +  sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1])**2)
	##if temp > max_dist:
	    ##furthest_pt = p
	    ##max_dist = temp
    ##if furthest_pt == []:
	##return
    ##pts.remove(furthest_pt)
    ##triangle = r + q + furthest_pt
    ##[set0, set1] = split_points(r, furthest_pt, q, pts)
    ##[set0, set2] = split_points(q, furthest_pt, r, pts)
    ##quick_hull(set1, r, furthest_pt)
    ##quick_hull(set2, furthest_pt, q)

def main():
    listPts = readDataPts('A_3000.dat', 3000)  #File name, numPts given as example only
    #print(giftwrap(listPts))      #You may replace these three print statements
    #print (grahamscan(listPts))   #with any code for validating your outputs
    print (amethod(listPts))     

 
if __name__  ==  "__main__":
    main()
