def numPaths(arr):
    N = len(arr)
    K = int(input())
    
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j][0] = arr[i][j]
            elif i == N - 1 or j == N - 1:
                if k == 0:
                    dp[i][j][k] = 1
                else:
                    dp[i][j][k] = 0
            else:
                dp[i][j][k] = sum([dp[i + 1][j][k - arr[i][j]] for _ in range(K)]) + sum([dp[i][j + 1][k - arr[i][j]] for _ in range(K)])
    
    return dp[0][0][K]

# Read input from stdin
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(numPaths(arr))
