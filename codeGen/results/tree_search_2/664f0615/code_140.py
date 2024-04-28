def max_path_segment(v0, vf, t, delta):
    memo = {}

    def dfs(distance_left, speed, time_elapsed):
        if (distance_left, speed, time_elapsed) in memo:
            return memo[(distance_left, speed, time_elapsed)]

        if distance_left == 0:  # reached the end
            return time_elapsed

        max_length = 0
        for new_speed in range(min(vf, speed + delta), max(v0, speed - delta) + 1):
            remaining_time = t - time_elapsed
            next_length = dfs(distance_left - (speed - new_speed), new_speed, time_elapsed + 1)
            max_length = max(max_length, next_length)

        memo[(distance_left, speed, time_elapsed)] = max_length
        return max_length

    v0_range = range(min(v0, vf), max(v0, vf) + 1)
    for v in v0_range:
        result = dfs(t * (vf - v0) // (vf + delta), v, 0)
        print(result)

if __name__ == "__main__":
    v0, vf, t, delta = [int(x) for x in input().split()]
    max_path_segment(v0, vf, t, delta)
