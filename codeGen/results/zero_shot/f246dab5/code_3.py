# Read input
n = int(input())
trips = []
for _ in range(n):
    trips.append(int(input()))

# Initialize total cost and current ticket types
total_cost = 0
current_tickets = {'one_trip': 0, '90_minutes': 0, 'day_ticket': 0}

# Iterate over the trips
for trip_time in trips:
    # Find the optimal tickets for this trip
    if trip_time < 60:  # one minute or less
        current_tickets['one_trip'] += 1
    elif trip_time <= 90:  # up to 90 minutes
        current_tickets['90_minutes'] += 1
    else:
        current_tickets['day_ticket'] += 1

    # Update total cost
    if current_tickets['one_trip']:
        total_cost += min(current_tickets['one_trip'], (trip_time + 59) // 60)
    if current_tickets['90_minutes']:
        total_cost += min(current_tickets['90_minutes'], (trip_time - 1) // 90)
    if current_tickets['day_ticket']:
        total_cost += min(current_tickets['day_ticket'], trip_time // 1440)

# Print the result
print(total_cost)
