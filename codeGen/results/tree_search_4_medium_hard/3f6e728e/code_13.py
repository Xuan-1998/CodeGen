import sys

def solve(N, M, C):
    dp = [[0] * (M+1) for _ in range(C+1)]
    dp[0][0] = 1
    
    for i in range(1, N+1):
        for j in range(M+1):
            if i <= C:
                dp[i][j] = (dp[i-1][j] + sum(dp[k][min(j, M)] for k in range(i))) % (10**9 + 7)
    
    return ' '.join(map(str, [dp[i][M] for i in range(1, C+1)]))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        print(solve(N, M, C))
