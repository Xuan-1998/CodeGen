import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(n, -1, -1):
        if a[i] == 0:
            dp[i] = dp[n]
        else:
            dp[i] = dp[i-1] or dp[n-i-1]
    
    print("YES" if dp[0] else "NO")

if __name__ == "__main__":
    solve()
