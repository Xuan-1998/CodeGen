import sys

n = int(sys.stdin.readline())
trip_times = []
for _ in range(n):
    trip_times.append(int(sys.stdin.readline()))

tickets = [20, 50, 120]  # cost of each ticket type

fare = 0
last_ticket_used = 0
for t in sorted(trip_times):
    if t - last_ticket_used >= 90:
        fare += 50
        last_ticket_used += 90
    elif t - last_ticket_used >= 1:
        fare += 20
        last_ticket_used += 1
    else:
        # use the day ticket (120) for trips less than 1 minute long
        fare += 120

print(fare)
