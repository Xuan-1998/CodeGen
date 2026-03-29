def beautyContest(t, l, r):
    # Define the base case: f(1) = 0
    dp = [[-1] * (r + 1) for _ in range(l)]
    for i in range(l):
        dp[i][i] = 0

    total = 0
    for i in range(t):
        for j in range(l, r + 1):
            if dp[j - l][j - 1] != -1:
                # Calculate the number of comparisons needed to select the most beautiful participant from the current group
                new_state = (dp[j - l][j - 1] + i) % (10**9 + 7)
                for k in range(j, r + 1):
                    if dp[k - j][k - 1] == -1:
                        dp[k - j][k - 1] = new_state
                    total += dp[k - j][k - 1]
            else:
                break

    return int(total) % (10**9 + 7)

t, l, r = map(int, input().split())
print(beautyContest(t, l, r))
