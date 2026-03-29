import sys

n = int(sys.stdin.readline())
total_fare = 0

for _ in range(n):
    t_i = int(sys.stdin.readline())
    if t_i < 90:  # 90-minute ticket
        total_fare += 50
    elif t_i < 1440:  # daily ticket
        total_fare += 120
    else:  # single-trip ticket
        total_fare += 20

print(total_fare)
