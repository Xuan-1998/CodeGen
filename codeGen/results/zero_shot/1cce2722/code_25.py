n = int(input())
a = list(map(int, input().split()))
max_points = 0
for i in range(n):
    max_points += n // (2 * a[i] - 1)
print(max_points)
