initial_speed, final_speed = map(int, input().split())
time, max_change = map(int, input().split())

max_length = (final_speed - initial_speed) * time + (time - 1) * abs(initial_speed)
print(max_length)
