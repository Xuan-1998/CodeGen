initial_speed, final_speed = map(int, input().split())
time, max_change = map(int, input().split())

if initial_speed > final_speed:
    initial_speed, final_speed = final_speed, initial_speed
    time = time[::-1]
    max_change = -max_change

max_length = 0
for i in range(time-1):
    length = (final_speed - initial_speed) * (i+1)
    if abs(final_speed - initial_speed) > max_change:
        break
    max_length = max(max_length, length)

print(max_length)
