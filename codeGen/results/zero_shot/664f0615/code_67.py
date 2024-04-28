import sys

initial_speed, final_speed = map(int, sys.stdin.readline().split())
time, max_change = map(int, sys.stdin.readline().split())

max_length = (final_speed - initial_speed) // (max_change + 1) * (max_change + 1)
print(max_length)
