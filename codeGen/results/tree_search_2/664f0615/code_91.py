def max_path_length(initial_speed, final_speed, time, max_change):
    memo = {}
    
    def dfs(diff, t):
        if (diff, t) in memo:
            return memo[(diff, t)]
        
        if t == 0:
            return 0
        
        if diff <= 0:  # reached the initial speed
            return min(dfs(0, time - 1), abs(final_speed - initial_speed))
        
        if abs(diff - max_change) <= 0.01:  # within the allowed change in speed
            next_diff = dfs(max(-diff + 1, -max_change), t - 1)
            return min(next_diff, abs(final_speed - initial_speed)) + 1
        
        memo[(diff, t)] = min(dfs(min(diff - 1, max_change), t - 1), abs(final_speed - initial_speed)) + 1
        return memo[(diff, t)]
    
    return dfs(abs(initial_speed - final_speed), time) * (max(initial_speed, final_speed) if initial_speed > 0 else min(initial_speed, final_speed))
