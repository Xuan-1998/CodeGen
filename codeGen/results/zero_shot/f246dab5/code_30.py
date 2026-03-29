import sys
n = int(input())
total_fare = 0
previous_ticket_time = 0
one_trip_ticket = 20
ninety_minutes_ticket = 50
fourteen40_minutes_ticket = 120

for trip in range(n):
    trip_start_time = int(input())
    
    if trip_start_time - previous_ticket_time <= one_trip_ticket:
        total_fare += one_trip_ticket
    elif trip_start_time - previous_ticket_time <= ninety_minutes_ticket + one_trip_ticket:
        total_fare += ninety_minutes_ticket
    else:
        total_fare += fourteen40_minutes_ticket
        
    previous_ticket_time = trip_start_time

print(total_fare)
