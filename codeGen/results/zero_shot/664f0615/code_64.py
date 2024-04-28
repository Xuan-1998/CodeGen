speed_initial, speed_final = map(int, input().split())
time, max_speed_diff = map(int, input().split())

print((speed_final - speed_initial) // max_speed_diff + 1)
