from collections import defaultdict

def min_ops(arr):
    n = len(arr)
    memo = defaultdict(int)

    def dp(i):
        if i >= n:
            return 0
        if arr[i] == 0:
            return dp(i + 1)
        if memo[i]:
            return memo[i]
        res = float('inf')
        if arr[i] > 1:
            res = min(res, 1 + dp(i + 1), 1 + dp(n - i - 1))
        memo[i] = res
        return res

    total_ops = 0
    for i in range(n):
        total_ops += dp(i)

    if total_ops == n:
        print("YES")
    else:
        print("NO")

n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    min_ops(arr)
