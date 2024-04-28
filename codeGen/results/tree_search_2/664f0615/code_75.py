def max_path_length(initial_speed, final_speed, time, delta):
    memo = {}

    def dfs(time, initial_speed, final_speed):
        if (time, initial_speed) in memo:
            return memo[(time, initial_speed)]

        if time == 0:
            return 0

        speed_diff = abs(final_speed - initial_speed)
        if speed_diff > delta:
            return 0

        max_length = 0
        for i in range(initial_speed, final_speed + 1):
            if i <= final_speed and abs(i - final_speed) <= delta:
                length = dfs(time - 1, i, final_speed) + time * (i / 100)
                max_length = max(max_length, length)

        memo[(time, initial_speed)] = max_length
        return max_length

    return int(dfs(time, initial_speed, final_speed))

# Example usage:
initial_speed, final_speed, time, delta = map(int, input().split())
print(max_path_length(initial_speed, final_speed, time, delta))
