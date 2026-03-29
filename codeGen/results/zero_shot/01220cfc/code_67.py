n = int(input())
arr = list(map(int, input().split()))
maxReach = 0
for i in range(n):
    if i <= maxReach and i + arr[i] > maxReach:
        maxReach = i + arr[i]
if maxReach >= n - 1:
    print("Yes")
else:
    print("No")
