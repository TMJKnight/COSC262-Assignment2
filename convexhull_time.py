from convexhull import *
import time


def giftwrap_time(listPts, N):
    total_time = 0
    for _ in range(N):
        pts = listPts[:]
        
        # Start the clock
        start_time = time.clock()
        
        # Run the convex hull algorithm
        chull = giftwrap(pts)
        
        # Stop the clock and calculate the running time for the convex hull 
        # algorithm
        end_time = time.clock() - start_time
        
        # Sum the running time N times for multiple runs
        total_time += end_time
    
    # Returns the average running time for the convex hull algorithm
    return total_time / N


def grahamscan_time(listPts, N):
    total_time = 0
    for _ in range(N):
        pts = listPts[:]
        
        # Start the clock
        start_time = time.clock()
        
        # Run the convex hull algorithm
        chull = grahamscan(pts)
        
        # Stop the clock and calculate the running time for the convex hull 
        # algorithm        
        end_time = time.clock() - start_time
        
        # Sum the running time N times for multiple runs
        total_time += end_time
    
    # Returns the average running time for the convex hull algorithm
    return total_time / N


def amethod_time(listPts, N):
    total_time = 0
    for _ in range(N):
        pts = listPts[:]
        
        # Start the clock
        start_time = time.clock()
        
        # Run the convex hull algorithm
        chull = amethod(pts)
        
        # Stop the clock and calculate the running time for the convex hull 
        # algorithm        
        end_time = time.clock() - start_time
        
        # Sum the running time N times for multiple runs
        total_time += end_time
    
    # Returns the average running time for the convex hull algorithm
    return total_time / N

##Uncoment lines below to test algorithm times

print('\nGift Wrap')
print('Set A')
for n in range(3000, 30001, 3000):
    listPts = readDataPts('A_30000.dat', n)
    print(giftwrap_time(listPts, 10))

print('Set B')
for n in range(3000, 30001, 3000):
    listPts = readDataPts('B_30000.dat', n)
    print(giftwrap_time(listPts, 10))


print('\nGraham-Scan')
print('Set A')
for n in range(3000, 30001, 3000):
    listPts = readDataPts('A_30000.dat', n)
    print(grahamscan_time(listPts, 10))

print('Set B')
for n in range(3000, 30001, 3000):
    listPts = readDataPts('B_30000.dat', n)
    print(grahamscan_time(listPts, 10))


print('\nMonotone Chain')    
print('Set A')
for n in range(3000, 30001, 3000):
    listPts = readDataPts('A_30000.dat', n)
    print(amethod_time(listPts, 10))

print('Set B')
for n in range(3000, 30001, 3000):
    listPts = readDataPts('B_30000.dat', n)
    print(amethod_time(listPts, 10))


#listPts = readDataPts('A_30000.dat', 30000)
#print(giftwrap_time(listPts, 5))
#listPts = readDataPts('_30000.dat', 30000)
#print(grahamscan_time(listPts, 5))
#listPts = readDataPts('B_30000.dat', 30000)
#print(amethod_time(listPts, 5))