def max_path_length():
    initial_speed, final_speed = map(int, input().split())
    time, max_change = map(int, input().split())

    memo = {}

    for t in range(time + 1):
        if t == 0:
            memo[(t, max_change)] = 0
        elif t == 1:
            memo[(t, max_change)] = abs(final_speed - initial_speed)
        else:
            for c in range(-max_change, max_change + 1):
                if (t - 2, c) in memo and (c - abs(final_speed - initial_speed)) <= 0:
                    memo[(t, max_change)] = max(memo[(t, max_change)].get(t, 0), 
                                                abs(final_speed - initial_speed) * t + memo[(t - 1, c)])
                else:
                    memo[(t, max_change)] = abs(final_speed - initial_speed)

    return memo[(time, max_change)]

print(max_path_length())
