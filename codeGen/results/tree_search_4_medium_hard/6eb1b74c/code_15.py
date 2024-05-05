def color_text(t, S):
    n = len(S)
    dp = [[-1] * (n + 1) for _ in range(len(t) + 1)]

    for j in range(n + 1):
        if S[j - 1].count(t[0]) == 1:
            dp[0][j] = 0
        else:
            dp[0][j] = -1

    for i in range(1, len(t) + 1):
        for j in range(n + 1):
            if dp[i - 1][j] != -1 and t[i - 1:i - len(S[j - 1]) + 1] == S[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - len(S[j - 1])][j - 1] + 1)
            else:
                dp[i][j] = -1

    m = float('inf')
    for j in range(n, -1, -1):
        if dp[-1][j] != -1 and (dp[-1][j] < m or m == -1):
            m = dp[-1][j]
            break

    if m == -1:
        return -1
    else:
        for i in range(len(t) + 1):
            for j in range(n, -1, -1):
                if dp[i][j] >= m and (dp[i][j] < m or i == len(t)):
                    print((j, i))
                    break

# Example usage
t = input()
n = int(input())
S = [input() for _ in range(n)]

color_text(t, S)
