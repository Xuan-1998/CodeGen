def checkAB(s):
    n = len(s)
    prefix = min(len('AB'), len('BA')) - 1
    dp = [[False] * 2 for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i <= prefix:
            if s[i-1] in 'AB':
                dp[i][0] = True
            else:
                dp[i][1] = True
        else:
            if s[i-1] == 'A' and (dp[i-1][0] or dp[i-1][1]):
                dp[i][0] = True
            elif s[i-1] == 'B' and (dp[i-1][0] or dp[i-1][1]):
                dp[i][1] = True

    return "YES" if any(dp[i][0] and dp[i][1] for i in range(n + 1)) else "NO"


if __name__ == "__main__":
    s = input()
    print(checkAB(s))
