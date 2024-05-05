from collections import defaultdict

def solve():
    T = int(input())
    MOD = 10**9 + 7
    
    dp = defaultdict(int)
    dp[0, 0] = 1

    for _ in range(T):
        N, M, C = map(int, input().split())
        
        for i in range(N):
            U_i = int(input())

        for j in range(M):
            L_j = int(input())

        # Build the dp table
        for i in range(1, N+1):
            for j in range(1, M+1):
                if U_i > C:
                    break
                if L_j > C:
                    break
                if i == 0 and j == 0:
                    continue
                if i > 0 and j > 0:
                    dp[i, j] = (dp[i-1][j] + dp[i][j-1]) % MOD
                elif i > 0 and j == 0:
                    dp[i, j] = dp[i-1][j]
                else:
                    dp[i, j] = dp[i][j-1]

        # Print the result
        for i in range(C+1):
            print(dp[N, M] % MOD, end=' ')
        print()

if __name__ == '__main__':
    solve()
