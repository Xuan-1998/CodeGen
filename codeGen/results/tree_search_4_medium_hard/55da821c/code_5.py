===BEGIN CODE===
def min_replant_plants(n, m, plants):
    dp = [[float('inf')] * (m + 1) for _ in range(m + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        section = plants[i - 1][0]
        prev_section = plants[i - 2][0] if i > 1 else 0
        min_replanted = float('inf')

        for j in range(m + 1):
            if j == 0:
                min_replanted = 0
            elif section != j:
                min_replanted = min(min_replanted, dp[prev_section][j - 1] + (section != j))

        for k in range(1, m + 1):
            dp[section][k] = min(dp[section][k], dp[section][k - 1] + (section != k))
        section += 1

    return min(dp[m - 1])

===END CODE===
