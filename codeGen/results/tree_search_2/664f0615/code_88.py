def max_path_length(initial_speed, final_speed, time, max_change):
    memo = {}

    def dfs(speed, t):
        if (speed, t) in memo:
            return memo[(speed, t)]
        if speed == initial_speed or speed == final_speed:
            return 0
        if t == 1:
            return 0
        min_length = float('inf')
        for new_speed in range(min(initial_speed + max_change, final_speed), max(initial_speed - max_change, final_speed), -1):
            length = dfs(new_speed, t-1) + abs(speed - new_speed)
            if length < min_length:
                min_length = length
        memo[(speed, t)] = min_length
        return min_length

    return min(dfs(initial_speed, time), key=lambda x: x)

initial_speed, final_speed, time, max_change = map(int, input().split())
print(max_path_length(initial_speed, final_speed, time, max_change))
