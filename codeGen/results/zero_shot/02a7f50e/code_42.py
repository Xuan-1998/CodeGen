import sys
from heapq import heapify, heappop

def min_destroyed_beacons():
    n = int(sys.stdin.readline())
    positions = []
    
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        positions.append((-b, a))  # Store power level first to simulate max heap
    heapify(positions)
    
    destroyed_beacons = 0
    
    while len(positions) > 1:
        _, x = heappop(positions)  # Get the rightmost beacon
        y, _ = heappop(positions)  # Get the second-rightmost beacon
        
        if x < y:  # If the rightmost beacon's power range doesn't cover the second-rightmost beacon
            destroyed_beacons += 1
    
    return destroyed_beacons

print(min_destroyed_beacons())
