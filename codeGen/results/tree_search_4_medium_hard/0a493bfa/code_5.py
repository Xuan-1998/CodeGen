def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        subset_a = 0
        for j in range(i):
            if a[j] in b:
                subset_a |= 1 << j
        for j in range(m + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + f(a[:i], b[:j]))
    
    return dp[-1][-1]

def f(a, b):
    beauty = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            p = gcd(a[i], a[j])
            if p not in b:
                beauty += a[i] // p + a[j] // p
    return beauty

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(solve())
