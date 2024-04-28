import sys

def partition_max_times(arr):
    n = len(arr)
    dp = [[0]*(n//2+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(min(i, n//2)+1):
            total = sum(arr[:i])
            left_sum = 0
            max_times = 0
            for k in range(j):
                if total-arr[i-k-1]-left_sum == left_sum:
                    max_times = max(max_times, dp[k][j-1]+dp[i-k-1][n-j-1])
                left_sum += arr[i-k-1]
            dp[i][j] = max_times

    return dp[n][n//2]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(partition_max_times(arr))
