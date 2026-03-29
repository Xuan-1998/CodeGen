import sys

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    
    # Initialize the first row and column as 1, since an empty sequence has length 0.
    for i in range(n):
        dp[i][i] = 1
    
    max_length = 0
    count = 0
    
    for len_increasing_subsequence in range(2, n+1):
        for i in range(n - len_increasing_subsequence + 1):
            j = i + len_increasing_subsequence - 1
            
            # If the current element is greater than the previous one, 
            # then we can extend the increasing subsequence.
            if arr[j] > arr[j-1]:
                dp[i][j] = min(dp[(i+1)][(j-1)], dp[i][j-1]) + 1
            else:
                # If the current element is not greater than the previous one, 
                # then there's no increasing subsequence ending at j in the first i elements.
                dp[i][j] = max(dp[(i+1)][(j-1)], dp[i][j-1])
            
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                count = 1
            elif dp[i][j] == max_length:
                count += 1
    
    print(count)

# Read input from standard input
arr = list(map(int, input().split()))
longest_increasing_subsequences(arr)
