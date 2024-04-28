initial_speed, final_speed = map(int, input().split())
time, max_change = map(int, input().split())

max_length = 0
current_speed = initial_speed
length = 0

for _ in range(time):
    if current_speed == initial_speed:
        length += min(final_speed - current_speed, max_change)
    elif current_speed == final_speed:
        length += min(current_speed - initial_speed, max_change)
    else:
        length += max_change
    
    current_speed += (final_speed - initial_speed) // time
    max_length = max(max_length, length)

print(max_length)
