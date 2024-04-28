def max_path_length():
    # Read input from stdin
    initial_speed, final_speed = map(int, input().split())
    time, max_change = map(int, input().split())

    # Initialize memoization dictionary with default values
    dp = {(0, 0): 0}

    for t in range(1, time + 1):
        for change in range(-max_change, max_change + 1):
            if t == 1:
                speed = initial_speed
            elif t == time:
                speed = final_speed
            else:
                speed = (initial_speed + final_speed) // 2

            if (t - 1, speed + change) in dp:
                dp[(t, speed)] = max(dp.get((t - 1, speed), 0) + abs(speed - (speed + change)), dp.get((t - 1, speed + change), 0) + abs(speed - (speed + change)))
            else:
                dp[(t, speed)] = min(abs(initial_speed - speed), abs(final_speed - speed)) + max(0, dp.get((t - 1, speed), 0))

    # Print the maximum possible length of the path segment in meters
    print(max(dp.values()))

if __name__ == "__main__":
    max_path_length()
