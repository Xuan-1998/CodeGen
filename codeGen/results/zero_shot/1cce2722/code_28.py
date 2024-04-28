n = int(input())
a = list(map(int, input().split()))
max_points = 0
for i in range(n):
    points = 1
    for j in range(i+1, n):
        if a[j] == a[i]:
            break
        points += 1
    max_points = max(max_points, points)
print(max_points)
