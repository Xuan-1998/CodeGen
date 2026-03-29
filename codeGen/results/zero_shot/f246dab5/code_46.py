import sys

n = int(sys.stdin.readline())
used_tickets = []

for _ in range(n):
    t = int(sys.stdin.readline())
    used_tickets.append(t)

fare = [0] * n

for i, trip_time in enumerate(used_tickets):
    if i == 0:  # First trip
        fare[i] = 20  # One-trip ticket (default)
    elif trip_time - used_tickets[i-1] <= 90:
        fare[i] += 50  # 90-minute ticket
    else:
        fare[i] += 120  # One-day ticket

print(*fare, sep='\n')
