import heapq

def choose_capital():
    n = int(input())
    roads = []
    for _ in range(n - 1):
        si, ti = map(int, input().split())
        roads.append((si, ti))

    dp = {i: float('inf') for i in range(1, n)}
    dp[0] = 0
    pq = [(0, 0)]  # (dist, city)

    while pq:
        dist, city = heapq.heappop(pq)
        for neighbor in roads:
            if neighbor[0] == city:
                neighbor_city = neighbor[1]
            elif neighbor[1] == city:
                neighbor_city = neighbor[0]

            if dp[neighbor_city] > dp[city] + 1:
                dp[neighbor_city] = dp[city] + 1
                heapq.heappush(pq, (dp[neighbor_city], neighbor_city))

    min_reversals = float('inf')
    capital_cities = []
    for i in range(1, n):
        if dp[i] < min_reversals:
            min_reversals = dp[i]
            capital_cities = [i + 1]

        elif dp[i] == min_reversals:
            capital_cities.append(i + 1)

    print(min_reversals)
    print(' '.join(map(str, capital_cities)))

if __name__ == "__main__":
    choose_capital()
