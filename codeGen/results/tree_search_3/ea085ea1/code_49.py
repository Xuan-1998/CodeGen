from collections import defaultdict

def find_max_common_substrings(str1, str2):
    n = len(str1)
    
    # Create a dictionary to store the frequency of each character in str1
    char_freq = defaultdict(int)
    for char in str1:
        char_freq[char] += 1
    
    # Initialize dp table with zeros
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Fill the dp table using the sliding window approach
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Calculate the maximum number of common non-overlapping substrings
    max_common_substrings = 0
    for i in range(n, 0, -1):
        if str1[i - 1] == str2[n - i]:
            max_common_substrings += 1
            n -= i
    
    return max_common_substrings

# Read input from standard input
str1 = input()
str2 = input()

# Calculate and print the maximum number of common non-overlapping substrings
max_common_substrings = find_max_common_substrings(str1, str2)
print(max_common_substrings)

