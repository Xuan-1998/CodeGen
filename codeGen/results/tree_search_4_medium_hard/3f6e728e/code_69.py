import sys

def solve():
    T = int(input())
    memo = {}
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        dp = [[0] * (C + 1) for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            for j in range(1, min(i, M) + 1):
                if (i, j) not in memo:
                    dp[i][j] = sum(dp[i - 1][k] for k in range(min(i, j)))
                    memo[(i, j)] = dp[i][j]
                else:
                    dp[i][j] = memo[(i, j)]
        
        print(*dp[-1], sep=' ')

if __name__ == "__main__":
    solve()
