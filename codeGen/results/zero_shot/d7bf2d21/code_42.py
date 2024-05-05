def find_length_of_longest_increasing_subsequence(array):
    n = len(array)
    
    # Initialize a table to store the length of the longest increasing subsequence ending at each position
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Count the number of longest increasing subsequences
    max_length = max(dp)
    count = sum(1 for x in dp if x == max_length)
    
    return count

# Read input from stdin
input_array = list(map(int, input().split()))

# Calculate and print the result
print(find_length_of_longest_increasing_subsequence(input_array))
