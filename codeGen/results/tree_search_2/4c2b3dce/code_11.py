from collections import defaultdict

def has_non_overlapping_substrings(s):
    n = len(s)
    dp = defaultdict(bool)

    for i in range(n):
        if s[i:i+2] == 'AB':
            if i >= 2 and s[i-2:i] == 'BA':
                return "YES"
            dp[i] = True

    return "NO"


# Test the function
s = input()
print(has_non_overlapping_substrings(s))
