import sys

def count_stable_tables():
    T = int(input())
    MOD = 10**9 + 7
    
    for _ in range(T):
        N, M = map(int, input().split())
        
        # Initialize the table with base cases
        dp = [[0] * (M+1) for _ in range(N+1)]
        dp[0][j] = 1 for j in range(M+1)
        dp[i][0] = 1 for i in range(1, N+1)

        # Fill the table using state transition equation
        for i in range(1, N+1):
            for j in range(1, M+1):
                for k in range(i):
                    if sum(dp[k]) + j <= M:
                        dp[i][j] += dp[k][j-k]
                dp[i][j] %= MOD
        
        # Calculate the final answer
        ans = 0
        for i in range(1, N+1):
            ans += dp[i][M]
            ans %= MOD
        
        print(ans)

if __name__ == "__main__":
    count_stable_tables()
