import sys

def min_operations(arr):
    N = len(arr)
    max_val = max(arr)
    dp = [[sys.maxsize for _ in range(max_val + 1)] for _ in range(N)]

    dp[0][1] = 0  # base case: no operations needed to make the array strictly increasing

    for i in range(1, N):
        for j in range(1, max_val + 1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][k] + (arr[i-1] - k) for k in range(arr[i-1], j+1)) + 1

    return dp[N-1][max_val]

# Example usage
N = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))
