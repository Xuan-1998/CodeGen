# Read input
n = int(input())
beacons = []
for i in range(n):
    position, power = map(int, input().split())
    beacons.append((position, power))

# Sort beacons based on their positions and powers
beacons.sort(key=lambda x: (x[0], -x[1]))

# Initialize the result with 0
result = 0

# Iterate over the sorted beacons
for i in range(n):
    # Find the maximum beacon to the left of the current one
    max_left = 0
    for j in range(i-1, -1, -1):
        if beacons[j][0] <= beacons[i][0]:
            max_left = j
            break
    
    # Check if a beacon needs to be destroyed or not
    if i > 0 and beacons[max_left][1] < beacons[i-1][1]:
        result += 1

# Print the result
print(result)
