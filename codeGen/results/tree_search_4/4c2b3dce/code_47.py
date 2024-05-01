def check_string(s):
    dp = {"": "NO"}  # base case: empty string
    for i in range(len(s)):
        if s[i:i+2] == "AB" and (i-2 < 0 or s[i-2:i] != "BA"):
            dp[s[:i]] = "YES"
        elif s[i:i+2] == "BA" and (i-2 < 0 or s[i-2:i] != "AB"):
            dp[s[:i]] = "YES"
    return dp.get(s, "NO")  # return the result for the original string

# Read input from stdin
s = input()

# Print output to stdout
print(check_string(s))
