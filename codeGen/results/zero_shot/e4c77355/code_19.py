def find_LIS_length(input_array):
    n = len(input_array)
    
    # Initialize the dynamic programming table with False values
    dp = [[False] * n for _ in range(n)]
    
    # Initialize the maximum length of the LIS
    max_length = 1
    
    # Fill the dynamic programming table
    for i in range(n):
        for j in range(i, n):
            if input_array[j] > input_array[i]:
                dp[i][j] = True
            else:
                break
            
            if j == n - 1 or not dp[i][j + 1]:
                max_length = max(max_length, j - i + 2)
    
    return max_length

# Read the input array from stdin
input_array = [int(x) for x in input().split()]

# Calculate and print the length of the longest increasing subsequence
print(find_LIS_length(input_array))
