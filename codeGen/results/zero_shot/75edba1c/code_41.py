import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(n):
    max_val = -float('inf')
    for j in range(i, n):
        max_val = max(max_val, arr[j])
        if max_val > k:
            ans += 1
print(ans)
