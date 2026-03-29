# Read input
n = int(input())
beacons = []
for _ in range(n):
    position, power = map(int, input().split())
    beacons.append((position, power))

# Sort the beacons by their positions
beacons.sort(key=lambda x: x[0])

# Initialize a list to keep track of the number of beacons destroyed for each activation point
destroyed = [0] * (n + 1)

# Iterate over the beacons and calculate the minimum number of beacons that could be destroyed
for i in range(n):
    # Calculate the power range of the current beacon
    power_range = beacons[i][1]
    
    # Initialize a variable to keep track of the maximum position within the power range
    max_position = beacons[i][0] + power_range
    
    # Iterate over the remaining beacons and calculate the minimum number of beacons that could be destroyed for each activation point
    for j in range(i, n):
        if beacons[j][0] <= max_position:
            destroyed[j + 1] = min(destroyed[j], i - j)
        else:
            break

# The answer is the maximum value in the 'destroyed' list minus one (since we want to add exactly one beacon)
print(max(destroyed) - 1)
