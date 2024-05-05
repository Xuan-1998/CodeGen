# Initialize variables
n = int(input())  # Number of trips
fare = 0  # Total fare charged so far
tickets = [20, 50, 120]  # Cost of one-trip, 90-minute, and daily tickets

for t in range(n):
    trip_time = int(input())  # Time of the current trip
    
    # Check if a daily ticket can be used for this trip
    if fare >= 120:
        fare -= 120
    else:
        # Calculate how many one-trip tickets are needed
        one_trip_tickets = (trip_time - fare) // 1
        fare += one_trip_tickets * 20
        
        # Calculate how many 90-minute tickets are needed
        ninety_minute_tickets = (trip_time - fare) // 90
        fare += ninety_minute_tickets * 50

print(fare)
