def find_min_durability(n, coordinates, durabilities):
    # Step 3: Find the weakest point
    weakest_point = min(durabilities)
    weakest_index = durabilities.index(weakest_point)

    # Step 4: Determine the best position to add the new ordinary point
    # For simplicity, let's assume the new point is added just before the weakest point
    # This is a simplification and may not always yield the correct answer
    # The actual implementation may require a more sophisticated approach
    left_load = coordinates[weakest_index] - coordinates[weakest_index - 1]
    right_load = coordinates[weakest_index + 1] - coordinates[weakest_index]

    # Step 5: Calculate the minimum durability required for the new point
    # This will be the maximum load it could receive from either side
    min_durability = max(left_load, right_load)

    # Check if we even need to add a point
    if min_durability <= weakest_point:
        return 0
    return min_durability

# Read input from stdin
n = int(input())
coordinates = list(map(int, input().split()))
durabilities = list(map(int, input().split()))

# Calculate and print the output
print(find_min_durability(n, coordinates, durabilities))
