def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    
    max_length = 0
    
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i][j] = 1
                max_ending_here = 0
                for k in range(j, -1, -1):
                    if dp[k][k] == 1 and max_ending_here < dp[k][k]:
                        max_ending_here = dp[k][k]
                max_length = max(max_length, max_ending_here)
    
    return max_length

# Test the function
arr = [int(x) for x in input().split()]
print(longest_increasing_subsequences(arr))
