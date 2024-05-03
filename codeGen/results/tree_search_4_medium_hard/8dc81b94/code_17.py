import sys

def dp(i):
    if i == 0:
        return 0
    if arr[i] - arr[0] > 0:
        return dp(i-1) + (arr[i] - arr[0])
    elif i < n-1 and arr[i] - arr[-1] > 0:
        return min(dp(i-1) + (arr[i] - arr[0]), dp(i+1) + (arr[i] - arr[-1]))
    else:
        return 0

n = int(input())
for _ in range(n):
    n, = map(int, input().split())
    arr = list(map(int, input().split()))
    print('YES' if dp(n-1) != sys.maxsize else 'NO')
