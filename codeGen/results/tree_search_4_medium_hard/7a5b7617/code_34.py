import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    MOD = 10**9 + 7
    dp = [[0] * (2001) for _ in range(2001)]
    dp[0][0] = 1
    
    for i in range(2*2000):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = 1
            elif j <= i:
                dp[i][j] = (dp[i-1][i-j] + dp[i-1][M-j-1]) % MOD
    
    for _ in range(T):
        N, M = map(int, input().split())
        print(dp[N][M])

if __name__ == "__main__":
    solve()
