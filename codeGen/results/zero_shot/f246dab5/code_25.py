import sys

n = int(sys.stdin.readline())
min_fare = 0
total_fare = 0

for _ in range(n):
    t = int(sys.stdin.readline())
    if t <= 1:
        min_fare = 20
    elif t <= 90:
        min_fare = 50
    else:
        min_fare = 120
    total_fare += min_fare

print(total_fare)
