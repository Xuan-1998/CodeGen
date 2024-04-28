def max_length(min_speed, max_speed, time_allowed, delta_v):
    dp = {i: -float('inf') for i in range(min_speed, max_speed + 1)}

    def recursive_max_length(v, t):
        if t <= 0 or v == min_speed or v == max_speed:
            return 0

        if dp[v] != -float('inf'):
            return dp[v]

        length = 0
        for i in range(1, time_allowed + 1):
            new_v = min(max(v + delta_v, min_speed), max_speed)
            length += 1
            if t - i >= 0:
                length += recursive_max_length(new_v, t - i)

        dp[v] = length
        return length

    return recursive_max_length(min_speed, time_allowed)

# Example input
min_speed, max_speed, time_allowed, delta_v = map(int, input().split())

print(max_length(min_speed, max_speed, time_allowed, delta_v))
