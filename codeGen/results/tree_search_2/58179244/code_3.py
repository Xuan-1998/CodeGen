from collections import defaultdict

def min_recolor(s):
    n = len(s)
    dp = [[float('inf')] * 3 for _ in range(n + 1)]
    dp[0][0] = 0  # base case: no recolors needed for an empty garland

    for i in range(1, n + 1):
        for c in 'RGB':
            if s[i - 1] == c:
                # if the current lamp has the same color as the previous one,
                # we need to recolor it
                dp[i][ord(c) - ord('R')] = min(dp[i][ord(c) - ord('R')], dp[i - 1][0] + 1)
            else:
                # if the current lamp has a different color from the previous one,
                # we don't need to recolor it
                dp[i][ord(c) - ord('R')] = dp[i - 1][ord(s[i - 1]) - ord('R')]

    min_recolors = float('inf')
    diverse_garland = ''

    for c in 'RGB':
        if dp[n][ord(c) - ord('R')] < min_recolors:
            min_recolors = dp[n][ord(c) - ord('R')]
            diverse_garland = ''.join([c if i < n and s[i] != c else s[i] for i in range(n)])

    return str(min_recolors), diverse_garland

# Example usage
n, s = map(str, input().split())
print(*min_recolor(s))
