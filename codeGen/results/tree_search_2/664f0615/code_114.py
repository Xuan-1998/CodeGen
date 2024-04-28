def max_length(initial_speed, final_speed, time, max_change):
    memo = {}

    def dp(t, change):
        if (t, change) in memo:
            return memo[(t, change)]

        if t == 1:
            # base case: only one second left
            speed = initial_speed + (final_speed - initial_speed) * t / time
            return min(time, int(10e6) // speed) * speed

        max_len = float('inf')
        for new_speed in range(initial_speed, final_speed):
            if abs(new_speed - initial_speed) <= change:
                # update the maximum length with the new speed and the remaining time
                len_ = dp(t-1, min(change, abs(new_speed - initial)))
                max_len = min(max_len, len_ + (new_speed * time // 10e6))

        memo[(t, change)] = max_len
        return max_len

    return dp(time, max_change)
