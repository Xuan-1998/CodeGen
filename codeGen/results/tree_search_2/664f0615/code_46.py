def dp(initial_speed, final_speed, time, max_change):
    dp = {}

    def dfs(current_speed, current_time):
        if (current_time, current_speed) in dp:
            return dp[(current_time, current_speed)]
        
        if current_time == 0:
            return 0

        next_speed = min(final_speed, max(initial_speed, current_speed + max_change))
        dp[(current_time, current_speed)] = dfs(next_speed, current_time - 1) + abs(next_speed - current_speed)
        return dp[(current_time, current_speed)]

    return dfs(initial_speed, time)

initial_speed, final_speed = map(int, input().split())
time, max_change = map(int, input().split())

print(dp(initial_speed, final_speed, time, max_change))
