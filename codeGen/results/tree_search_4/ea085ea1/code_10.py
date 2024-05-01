from collections import defaultdict

def common_substrings(str1, str2):
    # Create a dictionary to store the occurrences of each substring in both strings
    substrings = defaultdict(list)
    
    for i in range(len(str1)):
        for j in range(i+1, len(str1)+1):
            s1 = str1[i:j]
            
            if s1 in str2:
                substrings[s1].append((i, j))
    
    # Initialize the DP table with zeros
    dp = [[0] * (len(str1) + 1) for _ in range(len(str1) + 1)]
    
    max_count = 0
    
    for i in range(1, len(str1)+1):
        for k in range(i+1):
            if str1[k:i] in substrings:
                for j in range(len(str2)):
                    if str2[j:j+len(str1[k:i])] == str1[k:i]:
                        dp[i][k] = max(dp[j-1][k-1] + 1, dp[i][k])
                        max_count = max(max_count, dp[i][k])
    
    return max_count

# Read the input strings from standard input
str1 = input().strip()
str2 = input().strip()

print(common_substrings(str1, str2))
