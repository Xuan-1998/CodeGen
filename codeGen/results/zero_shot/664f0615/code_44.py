import sys

v0, vf = map(int, input().split())
t, d = map(int, input().split())

max_speed_diff = abs(vf - v0)
speed_range = (v0 + max_speed_diff, vf - max_speed_diff)

print((vf - v0) * t // max_speed_diff)
