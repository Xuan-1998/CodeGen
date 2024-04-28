def count_paths(arr, K, N):
    dp = [[0] * (N+1) for _ in range(N+1)]

    def dfs(i, j, k):
        if i == N-1 and j == N-1:
            return 1 if arr[i][j] == k else 0
        if dp[i][j]:
            return dp[i][j]

        ans = 0
        if i < N-1:
            ans += dfs(i+1, j, k-(arr[i][j]+1) if k >= arr[i][j] + 1 else -float('inf'))
        if j < N-1:
            ans += dfs(i, j+1, k-(arr[i][j]+1) if k >= arr[i][j] + 1 else -float('inf'))

        dp[i][j] = ans
        return ans

    return dfs(0, 0, K)

# Read input from stdin
K, N = map(int, input().split())
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

print(count_paths(arr, K, N))
