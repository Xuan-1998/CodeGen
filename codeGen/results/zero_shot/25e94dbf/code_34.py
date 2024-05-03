import sys

commands = input().strip()
n = int(input())

max_dist = max_distance(commands, n)

print(max_dist)
