from collections import defaultdict

def min_rec_colors(n, s):
    dp = [[float('inf')] * 3 for _ in range(n + 1)]

    # base case: if n is less than or equal to 2, we only need to recolor one lamp
    dp[0][s[0] == 'R'] = 1
    dp[1][s[0] != s[1]] = 1

    for i in range(2, n + 1):
        for j in range(3):
            # if the current color is the same as the previous one and not the same as the first color
            if (j == s[i - 1] == s[0]) or (s[0] != 'R' and j == 0) or (s[0] != 'G' and j == 1) or (s[0] != 'B' and j == 2):
                dp[i][j] = min(dp[i - 1][k] for k in range(3)) + 1
            else:
                dp[i][j] = min(dp[i - 1][k] for k in range(3))

    # return the minimum number of recolors needed to obtain a diverse garland
    return min(dp[-1])

# example usage
n, s = map(str, input().split())
print(min_rec_colors(n, s))
