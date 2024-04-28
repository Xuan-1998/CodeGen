initial_speed, final_speed = map(int, input().split())
time, speed_diff = map(int, input().split())

speed_range = abs(final_speed - initial_speed)
max_length = (time - 1) * speed_diff + min(initial_speed, final_speed)

print(max_length)
