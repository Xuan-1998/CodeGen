initial_speed, final_speed = map(int, input().split())
time, max_allowed_change = map(int, input().split())

total_distance = (final_speed + initial_speed) * time // 2
max_length = min(initial_speed * time, final_speed * time, total_distance)

print(max_length)
