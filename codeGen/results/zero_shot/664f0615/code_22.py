initial_speed, final_speed = map(int, input().split())
time, max_change = map(int, input().split())

total_distance = (final_speed + initial_speed) * time // 2
print(total_distance)
