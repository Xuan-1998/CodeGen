import heapq

def min_destruction(n):
    beacons = []
    
    # Read input
    for _ in range(n):
        x, y = map(int, input().split())
        
        # Calculate the area destroyed by this beacon
        destroyed_area = 0
        
        while beacons and beacons[0][1] <= y:
            destroyed_area += len(beacons)
            heapq.heappop(beacons)
        
        # Add the new beacon
        heapq.heappush(beacons, (x + y, x))
        
    return destroyed_area

n = int(input())
print(min_destruction(n))
