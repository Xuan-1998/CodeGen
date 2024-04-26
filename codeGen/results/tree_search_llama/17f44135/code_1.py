import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ans = 0
i = j = 0
while i < n and j < n:
    if arr[i] <= k:
        ans += 1
        i += 1
    elif arr[j] <= k:
        ans += 1
        j += 1
    else:
        break

print(ans)
