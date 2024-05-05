# Read the number of trips
n = int(input())

fare_dict = {1: 20, 90: 50, 1440: 120}
total_fare = 0

for _ in range(n):
    trip_time = int(input())
    
    # Find the ticket that can be used for this trip
    for time, fare in fare_dict.items():
        if trip_time <= time:
            total_fare += fare
            break
    
print(total_fare)
