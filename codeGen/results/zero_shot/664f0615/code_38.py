import sys

initial_speed, final_speed = map(int, input().split())
time, max_change = map(int, input().split())

max_length = (final_speed - initial_speed) / max_change
max_length *= time - 1
max_length += min(initial_speed, final_speed) * time

print(max_length)
