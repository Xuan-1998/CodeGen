import sys

def can_build(durability, points, durabilities):
    max_reach = [0] * len(points)
    max_reach[0] = points[0] + durabilities[0]
    max_reach[-1] = points[-1] - durabilities[-1]

    for i in range(1, len(points) - 1):
        max_reach[i] = min(points[i] + durabilities[i], max_reach[i - 1] + durability)

    for i in range(len(points) - 2, 0, -1):
        max_reach[i] = min(max_reach[i], points[i + 1] - durabilities[i + 1])

    for i in range(1, len(points)):
        if max_reach[i - 1] < points[i - 1] or max_reach[i] > points[i]:
            return False

    return True

def find_min_durability(n, points, durabilities):
    left, right = 0, points[-1] - points[0]
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_build(mid, points, durabilities):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

# Read input
n = int(input().strip())
points = list(map(int, input().strip().split()))
durabilities = list(map(int, input().strip().split()))

# Find and print the minimum durability
min_durability = find_min_durability(n, points, durabilities)
print(min_durability)
