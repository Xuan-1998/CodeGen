def min_operations(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    # Initialize dp[0] to 0, as there are no operations needed to make an empty array strictly increasing.
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(dp[i - 1], dp[i - 2] + (arr[i - 1] > arr[i]))
    
    return dp[-1]

# Read input
n = int(input())
arr = list(map(int, input().split()))

print(min_operations(arr))
