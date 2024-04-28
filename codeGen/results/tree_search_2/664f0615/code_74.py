def max_path_length(initial_speed, final_speed, time_taken, max_change):
    n = time_taken + 1
    dp = [[0] * (final_speed - initial_speed + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(min(final_speed, initial_speed + i * max_change), final_speed - initial_speed, -1):
            if j == initial_speed:
                dp[i][j - initial_speed] = 1
            elif j < initial_speed:
                dp[i][j - initial_speed] = dp[i-1][j - initial_speed]
            else:
                dp[i][j - initial_speed] = max(dp[i-1][j - initial_speed], dp[i-1][j - initial_speed - 1] + 1)

    return sum(range(initial_speed, final_speed + 1))

initial_speed, final_speed, time_taken, max_change = [int(x) for x in input().split()]
print(max_path_length(initial_speed, final_speed, time_taken, max_change))
