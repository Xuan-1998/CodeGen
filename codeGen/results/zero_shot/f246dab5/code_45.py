def calculate_fare(trips):
    fare = 0
    last_ticket_type = 'one-trip'
    for t in trips:
        if last_ticket_type == 'one-trip' and t <= 19:
            fare += 20
        elif last_ticket_type == 'one-trip' and t > 19:
            fare += 50
            last_ticket_type = '90-minutes'
        elif last_ticket_type == '90-minutes' and t <= 89:
            fare += 50
        elif last_ticket_type == '90-minutes' and t > 89:
            fare += 120
            last_ticket_type = 'day-long'

    return fare

n = int(input())
trips = []
for _ in range(n):
    trips.append(int(input()))

fare = calculate_fare(trips)
print(fare)
