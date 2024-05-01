from collections import defaultdict

def check_string(s):
    ab = 'AB'
    ba = 'BA'
    
    # Check for edge cases
    if len(s) < 2:
        return "NO"
    
    dp = defaultdict(bool)
    dp[0] = False
    
    for i in range(len(s)):
        for j in range(2):
            if s[i] == ab[j]:
                dp[i+1] = (dp[i]+((j==0) and 'AB' in s[:i])) or ((j==1) and 'BA' in s[:i])
    
    # Check if the string contains both 'AB' and 'BA'
    return "YES" if (ab in s and ba in s[len(s)-len(ab):]) else "NO"
