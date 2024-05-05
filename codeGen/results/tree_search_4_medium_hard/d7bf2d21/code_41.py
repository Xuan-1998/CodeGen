import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    
    # Initialize dp array with zeros
    dp = [0] * n
    
    # Initialize count array with zeros
    cnt = [0] * (sys.maxsize + 1)  # Assuming max possible length is n-1

    # Fill up the dp array using bottom-up approach
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Count the number of maximum length subsequences
    for i in range(n):
        cnt[dp[i]] += 1

    return sum(1 for k in cnt if k > 0)

# Read input from stdin
arr = [int(x) for x in input().split()]

print(longest_increasing_subsequence(arr))
