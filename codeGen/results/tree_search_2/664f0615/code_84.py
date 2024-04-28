def max_length_speed(initial_speed, final_speed, time, max_change):
    memo = {}

    def dfs(speed, t):
        if (speed, t) in memo:
            return memo[(speed, t)]
        if speed == final_speed and t == time:
            return 0
        if speed < final_speed or t > time:
            return float('inf')

        max_length = 0
        for new_speed in range(min(final_speed + 1, speed + max_change), max(initial_speed - 1, speed - max_change), -1):
            length = dfs(new_speed, t + 1)
            if length < float('inf'):
                max_length = max(max_length, length)

        memo[(speed, t)] = max_length
        return max_length

    return dfs(initial_speed, 0)

initial_speed, final_speed = map(int, input().split())
time, max_change = map(int, input().split())

print(max_length_speed(initial_speed, final_speed, time, max_change))
