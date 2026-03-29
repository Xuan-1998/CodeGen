from collections import defaultdict

def dp(n, m, k):
    if k == C:
        return 1
    if (n, m, k) in memo:
        return memo[(n, m, k)]
    
    res = 0
    for i in range(min(n, m), -1, -1):
        res += dp(n-i, m-i, k+1)
        res %= 10**9 + 7
    
    memo[(n, m, k)] = res
    return res

N, M, C = map(int, input().split())
U = list(map(int, input().split()))
L = list(map(int, input().split()))

memo = defaultdict(int)

print(dp(N, M, 0))
