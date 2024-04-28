def max_path_length():
    initial_speed, final_speed, time, speed_diff = map(int, input().split())
    dp = {(0, 0): 0}
    for _ in range(time):
        prev_dp = {}
        for diff, t in list(dp.items()):
            if abs(diff - speed_diff) <= speed_diff:
                new_t = t + 1
                prev_dp.setdefault(abs(new_t - time), 0)
                prev_dp[abs(new_t - time)] = max(prev_dp[abs(new_t - time)], dp.get((diff, t), 0))
        dp.update(prev_dp)
    return max(dp.values())

print(max_path_length())
