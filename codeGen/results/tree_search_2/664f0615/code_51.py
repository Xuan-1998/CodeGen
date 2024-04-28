def solve(initial_speed, final_speed, time, max_change):
    memo = {}

    def dfs(speed, t):
        if (speed, t) in memo:
            return memo[(speed, t)]
        
        if speed == initial_speed or speed == final_speed:
            if t == 1:
                return min(abs(speed - initial_speed), abs(speed - final_speed))
            else:
                return dfs(initial_speed, 1)
                # If the difference between the current and initial speeds is within the maximum allowed change,
                # then move to the initial speed. Similarly for the final speed.
        else:
            if t == 1:
                return min(abs(speed - initial_speed), abs(speed - final_speed))
            else:
                return max(dfs(initial_speed, 0) + abs(speed - initial_speed),
                           dfs(final_speed, 0) + abs(speed - final_speed))

        memo[(speed, t)] = result
        return result

    return dfs(initial_speed, 0)
