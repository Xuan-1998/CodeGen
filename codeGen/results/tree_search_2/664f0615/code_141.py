from sys import stdin

def max_length(initial_speed, final_speed, time_limit, speed_change):
    dp = {}

    def dfs(time, initial_speed):
        if (time, initial_speed) in dp:
            return dp[(time, initial_speed)]
        
        if time == 0:
            return 0
        
        result = 0
        for new_initial_speed in range(initial_speed - speed_change, initial_speed + speed_change + 1):
            remaining_time = time - 1
            result = max(result, dfs(remaining_time, new_initial_speed) + abs(new_initial_speed - initial_speed))
        
        dp[(time, initial_speed)] = result
        return result

    return dfs(time_limit, initial_speed)

initial_speed, final_speed = map(int, stdin.readline().split())
time_limit, speed_change = map(int, stdin.readline().split())

print(max_length(initial_speed, final_speed, time_limit, speed_change))
