init_speed, final_speed = map(int, input().split())
time, max_change = map(int, input().split())

speed_diff = final_speed - init_speed
max_length = 0

for i in range(time):
    if i == 0:
        speed = init_speed
    elif i == time-1:
        speed = final_speed
    else:
        speed = (init_speed + final_speed) // 2
    
    length = min(100, max(1, speed)) * 10
    max_length += length

max_length -= abs(speed_diff) * 10

print(max_length)
