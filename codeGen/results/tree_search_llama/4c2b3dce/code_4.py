def find_substrings():
    s = input()
    dp = [[False] * (len(s) + 1) for _ in range(2)]

    for i in range(len(s)):
        if s[i:i+2] == "AB":
            dp[0][i+2] = True
        elif s[i:i+2] == "BA":
            dp[1][i+2] = True

    for i in range(2, len(s) + 1):
        for j in range(i):
            if (dp[0][j] and dp[1][i]):
                return "YES"
    return "NO"

print(find_substrings())
