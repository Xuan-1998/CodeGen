initial_speed, final_speed = map(int, input().split())
time, max_change = map(int, input().split())

print(max(0, (final_speed - initial_speed) // max_change + 1))
