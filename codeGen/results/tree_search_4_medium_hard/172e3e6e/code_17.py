def solve(n, a):
    dp = [False] * n
    for i in range(1, n):
        if i > 0 and a[i] % i == 0:
            dp[i] = True
        elif dp[i-1]:
            dp[i] = (a[i] % len(dp[i-1]) == 0)
    res = sum(x for x in dp if x) % (10**9 + 7)
    return res

n = int(input())
a = [int(x) for x in input().split()]
print(solve(n, a))
