# Step 1: Read the input
n = int(input())
beacons = []
for _ in range(n):
    position, power = map(int, input().split())
    beacons.append((position, power))

# Step 2: Sort the beacons by their positions
beacons.sort()

# Step 3: Initialize a variable to store the minimum number of beacons that could be destroyed
min_destroyed = 0

# Step 4: Iterate over the sorted beacons and calculate the minimum number of beacons that could be destroyed
for i in range(n):
    for j in range(i+1, n):
        if beacons[j][0] - beacons[i][0] > beacons[i][1]:
            min_destroyed = max(min_destroyed, 1 + sum(1 for k in range(j) if beacons[k][0] <= beacons[i][0]))
            break

# Step 5: Print the minimum number of beacons that could be destroyed
print(min_destroyed)
