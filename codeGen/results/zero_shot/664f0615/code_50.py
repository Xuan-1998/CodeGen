initial_speed, final_speed = map(int, input().split())
time, max_allowed_change = map(int, input().split())

max_possible_length = (final_speed - initial_speed) * time + min(initial_speed * time, final_speed * time)

print(max_possible_length)
