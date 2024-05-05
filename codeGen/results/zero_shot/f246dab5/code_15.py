import sys

def calculate_fare(n):
    fares = []
    current_day_start_time = 0
    for i in range(n):
        trip_time = int(sys.stdin.readline())
        if trip_time <= current_day_start_time + 1440:  # same day or earlier
            fare = (trip_time - current_day_start_time) // 90 * 50 + (1440 - trip_time) % 90 * 20
        else:
            fare = (current_day_start_time + 1440 - trip_time) // 1440 * 120 + (trip_time - current_day_start_time) % 1440
        fares.append(fare)
        current_day_start_time = trip_time
    for fare in fares:
        print(fare, end=' ')
    print()
