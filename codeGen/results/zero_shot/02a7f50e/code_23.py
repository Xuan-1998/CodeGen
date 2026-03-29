# Step 1: Read input
n = int(input())  # number of beacons
beacons = []
for _ in range(n):
    x, y = map(int, input().split())
    beacons.append((x, y))

# Step 2: Sort beacons by position and then by power level (descending)
beacons.sort(key=lambda x: (x[0], -x[1]))

# Step 3: Initialize the minimum number of destroyed beacons
min_destroyed = n

# Step 4: Iterate over all possible positions for the new beacon
for i in range(n):
    # Add a new beacon with position i and power level to its right
    new_beacon = (i, max(beacon[1] for beacon in beacons[i+1:]))
    beacons.append(new_beacon)

    # Step 5: Calculate the minimum number of destroyed beacons with the new beacon added
    destroy_count = 0
    current_power = 0
    for i, (x, y) in enumerate(beacons):
        if x > i:
            continue
        if y <= current_power:
            destroy_count += 1
        else:
            current_power = y

    # Update the minimum number of destroyed beacons
    min_destroyed = min(min_destroyed, destroy_count)

    # Step 6: Remove the new beacon
    beacons.remove(new_beacon)

# Print the result
print(min_destroyed)
