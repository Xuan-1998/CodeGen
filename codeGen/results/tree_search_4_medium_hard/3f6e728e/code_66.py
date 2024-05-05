import sys

def main():
    T = int(input())
    
    MOD = 10**9 + 7
    
    dp = [[[0] * (C+1) for _ in range(M+1)] for _ in range(N+1)]
    
    for i in range(N+1):
        for j in range(M+1):
            if i == 0 and j == 0:
                dp[i][j][0] = 1
            else:
                for k in range(min(i, j), -1, -1):
                    dp[i][j][k+1] += (dp[i-k-1][j][k] * ((i+k+1) if k < C else 1)) % MOD
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        print(*[dp[N][M][c] for c in range(C+1)], sep=' ')

if __name__ == "__main__":
    main()
