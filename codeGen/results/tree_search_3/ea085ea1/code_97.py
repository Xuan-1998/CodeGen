code
from collections import defaultdict

def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        for j in range(i, N + 1):
            if str1[i - 1:j] == str2[:j - i]:
                dp[j] = max(dp[j], dp[i - 1] + 1)
    
    return dp[-1]

str1 = input().strip()
str2 = input().strip()

print(max_common_substrings(str1, str2))
