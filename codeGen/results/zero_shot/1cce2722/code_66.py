n = int(input())
a = list(map(int, input().split()))
max_points = 0
for i in range(n):
    points = 0
    k = a[i]
    while i-k-1 >= 0 and i+k+1 < n:
        a.pop(i-k-1)
        a.pop(i+k)
        points += 2
        k -= 1
    max_points = max(max_points, points + (i-n)//k + 1)
print(max_points)
