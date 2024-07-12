def minimize_removed_points(n, points):
    # Sort points by their position in descending order
    points.sort(reverse=True, key=lambda x: x[0])
    
    removed = set()
    min_removed = n

    for i in range(n):
        ai, bi = points[i]
        if ai not in removed:
            removed.add(ai)
            left_limit = ai - bi
            for j in range(i + 1, n):
                aj, _ = points[j]
                if aj > left_limit:
                    removed.add(aj)
    
    min_removed = len(removed)
    return min_removed

import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
points = []
for i in range(n):
    ai = int(data[2*i + 1])
    bi = int(data[2*i + 2])
    points.append((ai, bi))

result = minimize_removed_points(n, points)
print(result)

