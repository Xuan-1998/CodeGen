# Read the number of trips
n = int(input())

# Initialize an empty list to store the trip times
trip_times = []

# Read the trip times
for _ in range(n):
    trip_time = int(input())
    trip_times.append(trip_time)

# Sort the trip times in ascending order
trip_times.sort()

# Initialize variables to keep track of the fare charged so far
fare_charged = 0

# Initialize a variable to store the last used ticket type (0: one-trip, 1: 90-minute, 2: day-ticket)
last_used_ticket_type = -1

# Initialize a dictionary to store the tickets available at each time point
tickets_available = {i: [True, True, True] for i in range(10**9 + 1)}

# Iterate through the trip times
for i, trip_time in enumerate(trip_times):
    # Update the tickets available at the current time point
    while trip_time > 0:
        if last_used_ticket_type == 0 and tickets_available[trip_time][0]:
            fare_charged += 20
            last_used_ticket_type = 0
            trip_time -= 1
        elif last_used_ticket_type == 1 and tickets_available[trip_time][1]:
            fare_charged += 50
            last_used_ticket_type = 1
            trip_time -= 89
        elif last_used_ticket_type == 2 and tickets_available[trip_time][2]:
            fare_charged += 120
            last_used_ticket_type = 2
            trip_time -= 1399
        else:
            break
    
    # Print the fare charged for this trip
    print(fare_charged)
    
    # Update the fare charged for the next trip
    fare_charged = 0

# Close the program
exit()
