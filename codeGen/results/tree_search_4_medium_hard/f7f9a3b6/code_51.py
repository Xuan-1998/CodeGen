from collections import defaultdict

def solve():
    n = int(input())
    s = input()
    a = list(map(int, input().split()))
    
    # Initialize dp table
    dp = [[0] * 27 for _ in range(n + 1)]
    dp[0][0] = 1
    
    # Fill up the dp table
    for i in range(1, n + 1):
        for j in range(26):
            if s[i - 1].ord() == j + 96:
                dp[i][j + 1] += dp[i - 1][j]
            else:
                dp[i][j + 1] = dp[i - 1][j]
    
    # Find the number of ways to split the string
    ways_to_split = sum(dp[n][i] for i in range(26))
    
    # Find the length of the longest substring
    max_length = max(len(substring) for substring in s.split())
    
    # Find the minimum number of substrings
    min_substrings = 0
    current_length = 0
    for char in s:
        if a[ord(char) - 97] > 0 and (current_length == 0 or len(set(substring)) >= len(substring)):
            a[ord(char) - 97] -= 1
            current_length += 1
        else:
            min_substrings += 1
            current_length = 0
    
    return ways_to_split % (10 ** 9 + 7), max_length, min_substrings

print(*solve(), sep='\n')
