def max_length(initial_speed, final_speed, time, max_change):
    memo = {}

    def dfs(time, max_change):
        if (time, max_change) in memo:
            return memo[(time, max_change)]
        
        if time == 0:
            return 0
        
        if time < 0 or abs(final_speed - initial_speed) > max_change:
            return 0
        
        # The maximum length at this state is the minimum of
        # 1. The maximum length at the previous state (time-1, max_change)
        # 2. The speed at the last second being equal to the initial/final speed
        # 3. The maximum length at the state with time decreased by 1 and 
        #    the same maximum allowed change in speed
        
        prev_max_length = dfs(time - 1, max_change)
        
        if abs(initial_speed) <= max_change:
            max_length_with_initial = time
        else:
            max_length_with_initial = 0
        
        if abs(final_speed) <= max_change:
            max_length_with_final = time
        else:
            max_length_with_final = 0
        
        return min(prev_max_length, max_length_with_initial, max_length_with_final)

    return dfs(time, max_change)
