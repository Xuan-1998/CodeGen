def min_fare(trips):
    dp = {}
    total_cost = 0
    for i, t in enumerate(trips):
        num_tickets = (t // 90) + ((t % 90) > 0)
        if (i, num_tickets) not in dp:
            if i == 0:
                dp[(0, num_tickets)] = 20 * num_tickets + 50
            else:
                min_cost = float('inf')
                for j in range(max(0, num_tickets-1), -1, -1):
                    min_cost = min(min_cost, dp.get((i-1, j), 20*j) + (num_tickets > j)*50)
                dp[(i, num_tickets)] = min_cost
        total_cost += dp.get((i, num_tickets), float('inf'))
    return total_cost

if __name__ == "__main__":
    n = int(input())
    trips = []
    for _ in range(n):
        trips.append(int(input()))
    print(min_fare(trips))
