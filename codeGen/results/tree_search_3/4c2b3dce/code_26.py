def check_string(s):
    n = len(s)
    dp = [[False] * 2 for _ in range(n + 1)]

    for i in range(1, n + 1):
        if s[i - 1] == 'A':
            dp[i][0] = True
        elif s[i - 1] == 'B':
            dp[i][1] = True

    for i in range(n - 1, -1, -1):
        if dp[i][0]:
            if not dp[i + 1][1]:
                break
        elif dp[i][1]:
            if not dp[i + 1][0]:
                break

    return "YES" if (dp[0][0] and dp[-1][1]) or (dp[0][1] and dp[-1][0]) else "NO"


if __name__ == "__main__":
    s = input()
    print(check_string(s))
