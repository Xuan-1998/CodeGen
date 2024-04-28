import sys

initial_speed, final_speed = map(int, sys.stdin.readline().split())
time, speed_diff = map(int, sys.stdin.readline().split())

max_length = 0
speed = initial_speed

for _ in range(time):
    max_length += min(final_speed - speed, speed_diff)
    speed += min(final_speed - speed, speed_diff)

print(max_length)
