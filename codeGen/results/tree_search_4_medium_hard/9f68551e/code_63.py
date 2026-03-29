import sys

def solve():
    n = int(sys.stdin.readline().strip())
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        k, h = map(int, sys.stdin.readline().split())
        
        if h >= k:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(dp[i - 1], dp[max(0, i - k)] + (k - h))
    
    print(dp[-1])

if __name__ == "__main__":
    solve()
