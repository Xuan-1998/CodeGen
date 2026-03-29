from collections import defaultdict

def min_F(n, s, a):
    memo = defaultdict(int)

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 1:
            return min(x * (a[0] - x) for x in range(a[0] + 1))

        res = float('inf')
        for k in range(max(0, a[i-1] - s), min(s, a[i-1])):
            res = min(res, dp(i-1, j-k*a[i-1]+k))
        memo[(i, j)] = res
        return res

    res = 0
    for i in range(n):
        res += dp(i+1, s-a[i])
    return res

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_F(n, s, a))
