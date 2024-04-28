from functools import lru_cache

def max_path_length(initial_speed, final_speed, time, max_change):
    @lru_cache(None)
    def dfs(speed, t):
        if t > time:
            return 0
        if speed < initial_speed or speed > final_speed:
            return 0
        if t == time:
            return abs(final_speed - speed)
        
        next_speed = min(max(speed + max_change, initial_speed), final_speed)
        return max(dfs(next_speed, t + 1), dfs(speed, t + 1))

    return dfs(initial_speed, 1)

if __name__ == "__main__":
    initial, final, time, max_change = map(int, input().split())
    print(max_path_length(initial, final, time, max_change))
