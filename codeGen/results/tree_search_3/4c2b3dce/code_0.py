code
def has_abba_ba(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1):
        if s[i:i+2] == 'AB' and s[i+2:i+4] == 'BA':
            dp[i][i+3] = True

    for length in range(2, n + 1):
        for i in range(n - length):
            j = i + length
            if s[i:j] == 'ABBA' or (s[i:i+2] == 'AB' and dp[i+2][j-1]):
                dp[i][j] = True

    return "YES" if any(dp[0][n-1]) else "NO"


if __name__ == "__main__":
    s = input()
    print(has_abba_ba(s))
