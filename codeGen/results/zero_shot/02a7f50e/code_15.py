import sys

n = int(sys.stdin.readline())
beacons = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))

# Sort the beacons by their positions
beacons.sort()

min_destroyed = 0

for i in range(1, n):
    # Calculate the power level of the current beacon
    current_power = beacons[i-1][1]
    
    # Check if the current beacon can destroy any previous beacons
    for j in range(i-1, -1, -1):
        prev_power = beacons[j][1]
        
        if prev_power <= current_power:
            min_destroyed += 1
            break
    
print(min_destroyed)
