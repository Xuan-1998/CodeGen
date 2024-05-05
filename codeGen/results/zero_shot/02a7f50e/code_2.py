import sys
n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    pos, power = map(int, sys.stdin.readline().split())
    beacons.append((pos, power))

# Sort the beacons by position from right to left
beacons.sort(reverse=True)

# Initialize the result and the maximum power level seen so far
res = 0
max_power = 0

for pos, power in beacons:
    # If this beacon has a higher power level than any previously seen, 
    # we can add it without destroying any beacons. 
    if power > max_power:
        res += 1
    else:
        # Otherwise, find the rightmost beacon that will not be destroyed by this one.
        for i in range(res):
            if pos - beacons[i][0] <= power:
                break
        else:
            # If no such beacon is found, it means that all previously added beacons are destroyed.
            res += 1

print(res)
