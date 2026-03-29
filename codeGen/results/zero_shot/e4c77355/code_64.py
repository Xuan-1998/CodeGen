def longest_increasing_subsequence():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [1] * n  # Initialize dp array with all 1s (representing the length of increasing subsequences ending at each element)
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)  # Update dp array with the maximum length found so far
    
    return max(dp)

print(longest_increasing_subsequence())
