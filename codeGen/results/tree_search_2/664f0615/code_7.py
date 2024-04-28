def max_path_length():
    initial_speed, final_speed = map(int, input().split())
    time, max_change = map(int, input().split())

    dp = {}
    def dfs(speed, t):
        if (speed, t) in dp:
            return dp[(speed, t)]
        if t == 0:
            return 0
        if speed == initial_speed and t == time:
            return abs(initial_speed - final_speed)
        next_speeds = [max(0, min(final_speed, speed + max_change)), 
                        max(0, min(final_speed, speed - max_change))]
        next_lengths = []
        for ns in next_speeds:
            next_lengths.append(dfs(ns, t-1) + abs(initial_speed - ns))
        return max(next_lengths)

    print(dfs(initial_speed, time))

max_path_length()
