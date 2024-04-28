from collections import defaultdict

def max_length_of_path_segment():
    initial_speed, final_speed, time, max_change = [int(x) for x in input().split()]
    
    memo = defaultdict(int)
    memo[0, 0] = 0
    
    def dfs(time_left, speed):
        if (time_left, speed) in memo:
            return memo[(time_left, speed)]
        
        if time_left == 0:
            return 0
        
        if speed > final_speed:
            return dfs(time_left - 1, final_speed)
        
        next_speed = min(final_speed, speed + max_change)
        increase_length = dfs(time_left - 1, next_speed) + abs(next_speed - speed)
        decrease_length = dfs(time_left - 1, speed)
        
        memo[(time_left, speed)] = max(increase_length, decrease_length)
        
        return memo[(time_left, speed)]
    
    print(dfs(time, initial_speed))

if __name__ == "__main__":
    max_length_of_path_segment()
