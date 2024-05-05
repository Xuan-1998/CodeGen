import sys

n = int(sys.stdin.readline())
tickets = [20, 50, 120]

total_cost = 0
for t in range(n):
    trip_time = int(sys.stdin.readline())

    # Find the optimal ticket for this trip
    while tickets[-1] <= trip_time:
        tickets.pop()

    total_cost += tickets[0]
    print(total_cost)
