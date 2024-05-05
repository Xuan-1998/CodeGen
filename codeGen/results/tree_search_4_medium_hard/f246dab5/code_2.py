import heapq

def calculate_fare(n):
    # Initialize variables
    tickets = [(120, 0), (90, 50), (1, 20)]  # (duration, cost)
    pq = []  # priority queue to keep track of available tickets
    total_cost = 0

    for t in range(1, n+2):  # iterate over all trips and one extra for edge case
        while pq:
            minutes_left, cost_so_far = heapq.heappop(pq)
            if minutes_left >= t:  # use the ticket if it hasn't expired yet
                total_cost += cost_so_far
                break
        else:  # no suitable tickets found, start using new ones from earliest expiration time
            for duration, cost in tickets:
                if duration > t:  # this ticket won't expire before current trip ends
                    heapq.heappush(pq, (duration - t, total_cost + cost))
                    break

    return total_cost


# Example usage:
n = int(input())  # number of trips
print(calculate_fare(n))  # print the total fare charged after each trip
