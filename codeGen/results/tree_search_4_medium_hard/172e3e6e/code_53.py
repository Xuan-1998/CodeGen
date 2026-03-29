def count_good_subsequences():
    n = int(input())
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    
    dp = [[0] * (total_sum + 1) for _ in range(n + 1)]
    
    # Initialize the base case: an empty array is always a good subsequence
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(total_sum + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i-1][j]
            elif arr[i - 1] % i == 0:
                # If the current number is divisible by i, include it or not
                dp[i][j] = (dp[i-1][j//i] + dp[i-1][j]) % (10**9 + 7)
            else:
                # If the current number is not divisible by i, don't include it
                dp[i][j] = dp[i-1][j]
    
    # Count the number of good subsequences ending at the last position with sum total_sum
    return dp[n][total_sum]

print(count_good_subsequences())
