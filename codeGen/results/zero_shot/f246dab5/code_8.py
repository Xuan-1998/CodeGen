import sys

# Read input
n = int(sys.stdin.readline())
fares = []

for _ in range(n):
    t = int(sys.stdin.readline())
    one_trip_fare = 0
    ninety_minutes_fare = 0
    day_fare = 0

    # Calculate fares for each trip
    while t > 0:
        if t >= 1440:  # Day ticket
            day_fare += 120
            t -= 1440
        elif t >= 90:  # 90-minute ticket
            ninety_minutes_fare += 50
            t -= 90
        else:  # One-trip ticket
            one_trip_fare += 20
            t = 0

    fares.append(day_fare + ninety_minutes_fare + one_trip_fare)

# Print the results
for fare in fares:
    print(fare)
