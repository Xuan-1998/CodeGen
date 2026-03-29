# Step 1: Read input
n = int(input())
trips = []
for _ in range(n):
    trip_time = int(input())
    trips.append(trip_time)

# Step 2: Initialize fare and ticket counters
one_trip_fare = 0
ninety_min_fare = 0
fourteen_hour_fare = 0

# Step 3: Loop through each trip and calculate the fare
for i, trip in enumerate(trips):
    if trip <= 60:
        one_trip_fare += 1
    elif trip <= 150:
        ninety_min_fare += 1
        one_trip_fare -= 1
    else:
        fourteen_hour_fare += 1
        ninety_min_fare -= 14

# Step 4: Print the total fare for each trip
for i in range(n):
    if trips[i] <= 60:
        print(20)
    elif trips[i] <= 150:
        print(50 - (trips[i] - 60))
    else:
        print(120 - (trips[i] - 150))

