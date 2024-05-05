import sys

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    if n > sum(s):
        print(-1.0)
        return
    
    p = sum(si >= h for si in s) / len(s)
    
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i <= h:
            dp[i] = 1 - (1 - p)**i
        else:
            dp[i] = max(dp[i-1], 1 - (1 - p)*(n-i+1))
    
    print(dp[-1])

if __name__ == "__main__":
    solve()
