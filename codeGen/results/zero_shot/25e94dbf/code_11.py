import sys

commands = input().strip()
n = int(sys.stdin.readline())
distance = 0

for i in range(len(commands)):
    if commands[i] == 'F':
        distance += 1
    elif commands[i] == 'T':
        if n > 0:
            distance += 2
            n -= 1

print(distance)
