def calculate_fare(trips):
    # Initialize variables
    one_trip_tickets = 0
    ninety_minutes_tickets = 0
    day_tickets = 0
    
    # Calculate fares for each trip
    for i, t in enumerate(trips):
        if t <= 1:  # One-trip ticket
            one_trip_tickets += 20
        elif t <= 90 + 1:  # Ninety-minute ticket
            ninety_minutes_tickets += 50
        else:  # Day ticket
            day_tickets += 120
        
    return [one_trip_tickets, ninety_minutes_tickets, day_tickets]

# Read input from stdin
n = int(input())
trips = []
for i in range(n):
    t = int(input())
    trips.append(t)

# Calculate fares and print output to stdout
fares = calculate_fare(trips)
print(*fares, sep='\n')
