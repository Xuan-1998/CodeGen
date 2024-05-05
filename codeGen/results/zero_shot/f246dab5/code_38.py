import sys

n = int(sys.stdin.readline())
last_used_ticket_time = 0
total_cost = 0

for _ in range(n):
    trip_start_time = int(sys.stdin.readline())
    remaining_time = trip_start_time - last_used_ticket_time
    
    if remaining_time > 90:
        total_cost += 50
    elif remaining_time > 1:
        total_cost += 20
    else:
        total_cost += 20

    last_used_ticket_time = trip_start_time + 1

print(total_cost)
