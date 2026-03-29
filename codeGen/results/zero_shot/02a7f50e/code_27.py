import sys

# Step 1: Read input
n = int(sys.stdin.readline().strip())
beacons = []
for _ in range(n):
    position, power = map(int, sys.stdin.readline().strip().split())
    beacons.append((position, power))

# Step 2: Sort the beacons by their positions
beacons.sort()

# Step 3: Initialize a list to store the maximum power of the beacons that can be seen at each position
max_powers = [0] * (n + 1)

# Step 4: Iterate over the sorted beacons and calculate the maximum power of the beacons that can be seen at each position
for i in range(n):
    max_powers[i+1] = max(max_powers[i], beacons[i][1])

# Step 5: Calculate the minimum number of beacons that could be destroyed if exactly one beacon is added
min_destroyed = n - len([x for x in max_powers if x == max_powers[-1]])

print(min_destroyed)
