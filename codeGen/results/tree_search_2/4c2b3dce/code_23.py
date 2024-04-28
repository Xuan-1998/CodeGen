def find_ab_ba(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 2):
        for j in range(i + 3, n + 1):
            if s[i:i+2] == 'AB' and s[j-2:j] == 'BA':
                dp[i][j] = 1
            else:
                dp[i][j] = 0

    for i in range(n - 2):
        for j in range(i + 3, n + 1):
            if dp[i][j]:
                for k in range(i):
                    if dp[k][i]:
                        dp[k][j] = 1
                        break

    result = 'YES' if any(dp[0][n]) else 'NO'
    return result


import sys

s = input().strip()
print(find_ab_ba(s))
