import sys

n = int(sys.stdin.readline())
fares = []

for t in range(n):
    trip_time = int(sys.stdin.readline())
    if trip_time <= 90:  # one-trip ticket is sufficient
        fare = 20
    elif trip_time <= 1440:  # 90-minute ticket is sufficient
        fare = 50
    else:  # daily ticket is necessary
        fare = 120
    fares.append(fare)

for fare in fares:
    print(fare)
