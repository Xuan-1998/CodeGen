import sys

def solve(t, l, r):
    MOD = 10**9 + 7
    dp = [-1] * (r - l + 1)
    
    for i in range(l, r+1)[::-1]:
        if i % 2 == 0:
            dp[i-l] = dp[(i//2) - l] + i//2
        else:
            dp[i-l] = dp[(i+1)//2 - l] + 1
    
    res = t * (dp[0] + l)
    for i in range(1, len(dp)):
        res += t * dp[i]
    
    return int(res % MOD)

if __name__ == "__main__":
    t, l, r = map(int, input().split())
    print(solve(t, l, r))
