import sys

one_trip = 20
ninety_minutes = 50
one_day = 120

n = int(sys.stdin.readline())
total_cost = 0

for _ in range(n):
    t_i = int(sys.stdin.readline())
    if t_i <= 1:
        total_cost += one_trip
    elif t_i % 90 > 0:
        remaining_minutes = t_i % 90
        if remaining_minutes <= 1:
            total_cost += one_trip
        else:
            total_cost += ninety_minutes + one_trip
    else:
        total_cost += one_day

sys.stdout.write(str(total_cost) + '\n')
