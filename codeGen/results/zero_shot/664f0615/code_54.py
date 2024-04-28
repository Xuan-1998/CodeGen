import sys

init_speed, final_speed = map(int, input().split())
time_to_travel, max_allowed_change = map(int, input().split())

max_length = 0
for speed in range(init_speed, final_speed + 1):
    if abs(speed - init_speed) <= max_allowed_change and abs(final_speed - speed) <= max_allowed_change:
        max_length = max(max_length, time_to_travel * speed)

print(max_length)
