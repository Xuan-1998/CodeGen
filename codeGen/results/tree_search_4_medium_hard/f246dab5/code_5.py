import sys

def min_fare(trips):
    n = int(input())  # number of trips
    fares = [0] * (n + 1)  # initialize fare array with zeros

    tickets = [(1, 20), (90, 50), (1440, 120)]  # define ticket types and costs

    for i in range(1, n + 1):
        minutes_left_until_ticket_expires = trips[i - 1]
        total_cost_so_far = fares[i - 1]

        for j, cost in tickets:
            if minutes_left_until_ticket_expires >= j:
                new_minutes_left_until_ticket_expires = (minutes_left_until_ticket_expires - j)
                new_total_cost_so_far = total_cost_so_far + cost
                fares[i] = min(fares[i], new_total_cost_so_far)

    return fares[-1]

trips = []
while True:
    try:
        trip = int(input())
        trips.append(trip)
    except EOFError:
        break

print(min_fare(trips))
