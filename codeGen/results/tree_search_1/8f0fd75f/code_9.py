import sys

def can_support(points, durability, max_support_left, max_support_right, new_point_durability):
    # Simulate the addition of the new point with the guessed durability
    n = len(points) - 2
    left_support = [0] * n
    right_support = [0] * n
    
    # Calculate initial support ranges for each point
    for i in range(n):
        left_support[i] = min(max_support_left[i], points[i + 1] - points[i])
        right_support[i] = min(max_support_right[i], points[i + 2] - points[i + 1])

    # Simulate the collapse process
    for i in range(n - 1, -1, -1):
        # If the current point's right support is exceeded
        if right_support[i] < points[i + 2] - points[i + 1]:
            return False
        # Redistribute the load to the left
        if i > 0:
            right_support[i - 1] = min(right_support[i - 1], right_support[i] - (points[i + 1] - points[i]))

    for i in range(n):
        # If the current point's left support is exceeded
        if left_support[i] < points[i + 1] - points[i]:
            return False
        # Redistribute the load to the right
        if i < n - 1:
            left_support[i + 1] = min(left_support[i + 1], left_support[i] - (points[i + 2] - points[i + 1]))

    # Check if the new point can be added without collapsing the building
    for i in range(n):
        if left_support[i] + right_support[i] + new_point_durability >= points[i + 2] - points[i]:
            return True
    return False

def find_min_durability(points, durability):
    n = len(points) - 2
    max_support_left = durability[:]
    max_support_right = durability[:]

    # Perform binary search on the minimum durability required for the additional point
    low, high = 1, max(durability)
    result = high
    while low <= high:
        mid = (low + high) // 2
        if can_support(points, durability, max_support_left, max_support_right, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

# Read input
n = int(input().strip())
points = list(map(int, input().strip().split()))
durability = list(map(int, input().strip().split()))

# Find and print the minimum durability
min_durability = find_min_durability(points, durability)
print(min_durability)
