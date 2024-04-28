def max_length(initial_speed, final_speed, time, max_change):
    memo = {}

    def dfs(current_time, current_speed):
        if (current_time, current_speed) in memo:
            return memo[(current_time, current_speed)]

        if current_time == 0:
            return 0

        next_speed = min(final_speed, initial_speed + max(0, max_change - abs(initial_speed - current_speed)))
        distance = min((time - current_time) * (next_speed - current_speed), 1000)
        memo[(current_time, current_speed)] = dfs(current_time - 1, next_speed) + distance
        return memo[(current_time, current_speed)]

    return dfs(time, initial_speed)

initial_speed = int(input())
final_speed = int(input())
time = int(input())
max_change = int(input())

print(max_length(initial_speed, final_speed, time, max_change))
