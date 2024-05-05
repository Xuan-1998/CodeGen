import sys
from bisect import bisect_right

n = int(sys.stdin.readline())
beacons = [(int(line.split()[1]), int(line.split()[2])) for line in sys.stdin.readlines() if line]

def calculate_max_power(beacons):
    beacons.sort(reverse=True)
    max_power = 0
    destroyed = set()
    
    for a, b in beacons:
        i = bisect_right(destroyed, a) - 1
        while i >= 0 and (i == len(destroyed) - 1 or destroyed[i] < a):
            destroyed.pop(i)
            i -= 1
        
        max_power = max(max_power, b)
        
    return max_power

max_power = calculate_max_power(beacons)

print(min(n + 1, bisect_right([0] * n, 0) - bisect_right(sorted(destroyed), 0)))
