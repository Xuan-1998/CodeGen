def min_steps_to_color_text(t, s):
    n = len(s)
    dp = [[-1] * (n + 1) for _ in range(len(t) + 1)]

    # Initialize base case
    for j in range(n + 1):
        dp[0][j] = 0

    result = -1
    for i in range(1, len(t) + 1):
        for j in range(1, n + 1):
            if t[i - 1] not in [s[k][0] for k in range(j)]:
                dp[i][j] = dp[i - 1][j]
            else:
                for k in range(j):
                    if s[k][0] == t[i - 1]:
                        break
                dp[i][j] = min(dp[k][j - 1] + 1, dp[i][j])
            if dp[i][n] != -1:
                result = dp[i][n]
    if result == -1:
        return "Impossible to color the text"
    else:
        return str(result)

    # Print the steps
    for i in range(len(t), 0, -1):
        j = n
        while dp[i][j] != -1 and j > 0:
            for k in range(n):
                if s[k][0] == t[i - 1]:
                    print(f"({k}, {i})")
                    break
            j -= 1

    return result
