import sys

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    
    for i in range(h, -1, -1):
        for k in range(n, -1, -1):
            if s[i-1] >= n-k:
                dp[k] += (s[i-1] - (n-k)) / (m-i+1)
    
    prob = 0
    for i in range(1, n + 1):
        prob += dp[i]
    
    print(prob) if sum(s) >= n else sys.stdout.write('-1\n')

solve()
