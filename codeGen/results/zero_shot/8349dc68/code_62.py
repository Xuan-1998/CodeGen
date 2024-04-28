n = int(input())
arr = list(map(int, input().split()))
k = int(input())

ans = 0
total = 0
for i in range(0, n, k):
    total += max(arr[i:i+k])
    ans = max(ans, total)

print(ans)
