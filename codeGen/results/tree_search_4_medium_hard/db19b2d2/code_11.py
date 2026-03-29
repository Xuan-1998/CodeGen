import sys

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    if sum(s) < n:
        print(-1)
        return
    
    dp = [0] * (n + 1)
    dp[0] = 1 if h > 0 else 0
    for i in range(1, n + 1):
        for j in range(m):
            if s[j] == 0:
                continue
            if j == h - 1:
                dp[i] = min(dp[i], s[h-1]/sum(s) + (1 - s[h-1]/sum(s)) * dp[i-1])
            else:
                dp[i] = max(dp[i], dp[i-1] if dp[i-1] > 0 else 0)
    
    print(1 - dp[n])

if __name__ == "__main__":
    solve()
