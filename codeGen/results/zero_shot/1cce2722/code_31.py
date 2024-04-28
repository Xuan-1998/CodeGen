n = int(input())
a = list(map(int, input().split()))
max_points = 0
for i in range(n):
    points = 2 ** (i + 1) - 1
    max_points = max(max_points, points)
print(max_points)
