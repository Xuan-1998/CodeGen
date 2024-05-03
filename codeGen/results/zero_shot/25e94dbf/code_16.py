import sys

n = int(sys.stdin.readline().strip())
commands = list(sys.stdin.readline().strip())

max_distance = find_max_distance(commands, n)
print(max_distance)
