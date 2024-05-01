import sys

def check_string(s):
    if len(s) < 2:
        return "NO"

    dp = [False] * (len(s) + 1)
    dp[0] = False
    dp[1] = True if s[:2] == "AB" else False

    for i in range(2, len(s)):
        dp[i] = dp[i-1] or (s[i-1:i+1] == "BA" and dp[i-2])
    return "YES" if dp[-1] else "NO"

if __name__ == "__main__":
    s = input()
    print(check_string(s))
