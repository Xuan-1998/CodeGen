def longest_increasing_subsequence_length(arr):
    n = len(arr)
    
    # Initialize dp dictionary to store the length of the longest 
    # increasing subsequence ending at each index
    dp = {i: 1 for i in range(n)}
    memo = {}
    
    def dfs(i, prev):
        if (i, prev) in memo:
            return memo[(i, prev)]
        
        res = 0
        
        # If the current element is greater than the previous one, 
        # we can extend the subsequence
        if arr[i] > prev or prev is None:
            for j in range(i+1, n):
                if arr[j] > arr[i]:
                    res = max(res, dfs(j, arr[i]) + 1)
        
        memo[(i, prev)] = res
        return res
    
    # Calculate the length of the longest increasing subsequence ending at each index
    for i in range(n-1):
        dp[i+1] = max(dp[i], dfs(i+1, None))
    
    # The number of longest increasing subsequences is the maximum 
    # length minus one (because we're considering subsequences that end at each index)
    return max(dp.values()) - 1

# Read input from stdin
arr = list(map(int, input().split()))

print(longest_increasing_subsequence_length(arr))
