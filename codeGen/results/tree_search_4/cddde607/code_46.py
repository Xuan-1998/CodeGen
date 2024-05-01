def findPaths(K, N, arr):
    dp = [[[0]*2001 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[i][j] <= K:
                    dp[i][j][arr[i][j]] = 1
            elif i > 0:
                for k in range(arr[i][j]+1):
                    if k <= K:
                        dp[i][j][k] += dp[i-1][j][min(k, arr[i-1][j])]
            elif j > 0:
                for k in range(arr[i][j]+1):
                    if k <= K:
                        dp[i][j][k] += dp[i][j-1][max(0, k-arr[i][j])]

    return sum([dp[N-1][N-1][i] for i in range(K+1)])

if __name__ == "__main__":
    K = int(input())
    N = int(input())
    arr = [[int(x) for x in input().split()] for _ in range(N)]
    print(findPaths(K, N, arr))
