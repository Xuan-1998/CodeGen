import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [[0] * (10**6 + 7) for _ in range(n+1)]
    
    for i in range(1, n+1):
        last_divisor = a[i-1]
        for d in range(2, int(last_divisor ** 0.5) + 1):
            if last_divisor % d == 0:
                dp[i][d] = (dp[i-1][d] + dp[i-1][last_divisor//d]) % (10**9 + 7)
        dp[i][0] = (dp[i-1][0] + 1) % (10**9 + 7)
    
    print((sum(dp[i][0] for i in range(1, n+1)) + 1) % (10**9 + 7))

if __name__ == "__main__":
    solve()
