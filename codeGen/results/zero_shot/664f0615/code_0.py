init_speed, final_speed = map(int, input().split())
time, max_change_speed = map(int, input().split())

max_length = 0
for speed in range(init_speed, final_speed + 1):
    if abs(speed - init_speed) <= max_change_speed and abs(speed - final_speed) <= max_change_speed:
        max_length = max(max_length, (final_speed - init_speed + 1) * time)
print(max_length)
