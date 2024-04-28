init_speed, final_speed = map(int, input().split())
time, max_change = map(int, input().split())

max_length = (final_speed - init_speed) * time + 0.5
max_length -= max_change * time

print(max_length)
