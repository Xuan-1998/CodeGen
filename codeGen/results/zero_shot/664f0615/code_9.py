speed_initial, speed_final = map(int, input().split())
time, max_speed_diff = map(int, input().split())

max_length = (speed_final - speed_initial) * time + (speed_initial + speed_final) // 2
max_length -= abs(speed_initial - speed_final)

print(max_length)
