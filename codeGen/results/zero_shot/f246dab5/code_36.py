def min_cost(n):
    # Initialize variables
    one_trip_costs = [0] * (n + 1)
    ninety_minutes_costs = [0] * (n + 1)
    one_day_costs = [0] * (n + 1)

    # Calculate the minimum cost for each trip
    for i in range(1, n + 1):
        if i <= 90:
            one_trip_costs[i] = min(one_trip_costs[i-1], one_trip_costs[0])
        else:
            ninety_minutes_costs[i-90] += one_day_costs[i-90]
        if i >= 1440:
            one_day_costs[i] = min(one_day_costs[i-1], one_trip_costs[i-1440])

    # Return the minimum cost for all trips
    return sum(one_trip_costs + ninety_minutes_costs + one_day_costs)
