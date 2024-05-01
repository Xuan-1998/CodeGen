from sys import stdin

def count_paths(K, N, arr):
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = 1
    
    for i in range(N):
        for j in range(N):
            if i < N-1:
                dp[i+1][j] += dp[i][j]
            if j < N-1:
                dp[i][j+1] += dp[i][j]
            if arr[i][j] <= K:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) if i > 0 and j > 0 else 0
    
    return dp[N-1][N-1]

K, N = map(int, stdin.readline().split())
arr = []
for _ in range(N):
    row = list(map(int, stdin.readline().split()))
    arr.append(row)

print(count_paths(K, N, arr))
