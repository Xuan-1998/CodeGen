import sys

def lis(arr):
    n = len(arr)
    dp = [[1] * (max(arr) + 1) for _ in range(n)]

    for i in range(n):
        for j in range(min(arr), max(arr) + 1):
            if arr[i] == j:
                for k in range(i - 1, -1, -1):
                    if arr[k] < j and dp[k][j]:
                        dp[i][j] = max(dp[i][j], dp[k][j] + 1)

    return max(max(row) for row in dp)

# Read input from stdin
input_arr = [int(x) for x in sys.stdin.readline().split()]

print(lis(input_arr))
