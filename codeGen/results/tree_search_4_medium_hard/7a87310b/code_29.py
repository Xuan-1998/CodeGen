import sys

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0]*(N+1) for _ in range(N+1)]
        for i in range(1, N+1):
            for d in range(1, min(i+1, N)+1):
                if d > 0:
                    dp[i][d] = sum(dp[k][d-1] for k in range(1, min(i+1, d)))
                else:
                    dp[i][d] = 0
        print(sum(dp[i][j] for i in range(N, -1, -1) for j in range(1, N+1) if i+j==N and j>0))

if __name__ == "__main__":
    solve()
