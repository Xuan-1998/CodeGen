import sys

def find_lis_count(arr):
    n = len(arr)
    dp = [1] * (n + 1)

    for i in range(n):
        for j in range(i, n):
            if arr[j] > arr[i]:
                dp[j+1] = max(dp[j+1], dp[i]+1)

    return sum(1 for x in dp if x == max(dp))

# Read input from standard input
arr = list(map(int, input().split()))

print(find_lis_count(arr))
