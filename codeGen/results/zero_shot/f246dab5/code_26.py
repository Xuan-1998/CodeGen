import sys
from collections import defaultdict

n = int(sys.stdin.readline())
trip_times = []
for _ in range(n):
    trip_times.append(int(sys.stdin.readline()))

trip_times.sort()
used_tickets = defaultdict(list)

current_time = 0
total_fare = 0

for time in trip_times:
    if time - current_time >= 1440:  # one day ticket
        used_tickets[1440].append(time)
        total_fare += 120
        current_time = time
    elif time - current_time >= 90:  # 90 minutes ticket
        used_tickets[90].append(time)
        total_fare += 50
        current_time = time
    else:  # one trip ticket
        used_tickets[1].append(time)
        total_fare += 20

sys.stdout.write(str(total_fare) + '\n')
