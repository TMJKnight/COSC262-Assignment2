from convexhull import *
import time
def giftwrap_time(listPts, N):
    total_time = 0
    for _ in range(N):
        pts = listPts[:]
        start_time = time.clock()
        chull = giftwrap(pts)
        end_time = time.clock() - start_time
        total_time += end_time
    return total_time / N

def grahamscan_time(listPts, N):
    total_time = 0
    for _ in range(N):
        pts = listPts[:]
        start_time = time.clock()
        chull = grahamscan(pts)
        end_time = time.clock() - start_time
        total_time += end_time
    return total_time / N
        

listPts = readDataPts('A_3000.dat', 3000)
print(giftwrap_time(listPts, 5))
listPts = readDataPts('B_30000.dat', 30000)
#print(grahamscan_time(listPts, 5))