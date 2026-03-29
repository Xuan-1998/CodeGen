import sys

n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.read().strip().split()))
times.sort()

fare = 0
prev_time = 0
for time in times:
    if time - prev_time > 89:
        fare += 120
    elif time - prev_time > 19:
        fare += 50
    else:
        fare += 20
    prev_time = time

print(fare)
