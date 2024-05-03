import sys

def min_replants(n, m):
    plants = []
    for _ in range(n):
        _, x, s = map(int, input().split())
        plants.append((x, s))

    plants.sort()

    replants = 0
    for i in range(1, m):
        left, right = -float('inf'), float('inf')
        for j in range(len(plants)):
            if plants[j][1] == i:
                if plants[j][0] < left:
                    left = plants[j][0]
                if plants[j][0] > right:
                    right = plants[j][0]

        replants += (right - left)

    return int(replants) + m - 1

n, m = map(int, input().split())
print(min_replants(n, m))
