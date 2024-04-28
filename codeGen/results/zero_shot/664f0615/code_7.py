initial_speed, final_speed = map(int, input().split())
time, max_speed_change = map(int, input().split())

max_length = (final_speed - initial_speed) * time // max_speed_change + 1
print(max_length)
