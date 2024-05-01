import sys

def check_string(s):
    n = len(s)
    dp = [False] * (n + 1)

    for i in range(n + 1):
        if i < 3:
            dp[i] = True
        else:
            if s[i - 3:i].endswith('AB') and dp[i - 3]:
                dp[i] = True
            elif s[i - 2:i].endswith('BA') and dp[i - 2]:
                dp[i] = True

    return "YES" if dp[n] else "NO"


if __name__ == "__main__":
    s = input().strip()
    print(check_string(s))
