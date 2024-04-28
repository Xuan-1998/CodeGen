def max_length(time_left, init_speed, fin_speed):
    if time_left <= 0:
        return 0

    max_len = float('-inf')

    for new_speed in range(min(init_speed, fin_speed), max(init_speed, fin_speed) + 1):
        if abs(new_speed - init_speed) > max_change or abs(new_speed - fin_speed) > max_change:
            continue
        len_left = time_left - 1
        max_len = max(max_len, new_speed * (time_left - 1) + max_length(len_left, init_speed, new_speed))
    return max_len

max_change, init_speed, fin_speed, time = map(int, input().split())
print(max_length(time, init_speed, fin_speed))
