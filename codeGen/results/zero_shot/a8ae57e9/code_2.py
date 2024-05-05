import sys

def solve():
    n, k = map(int, input().split())
    requests = []
    for _ in range(n):
        size, amount = map(int, input().split())
        requests.append((size, amount))

    requests.sort(key=lambda x: x[1], reverse=True)

    total_earned = 0
    table_capacities = [0] * k

    accepted_requests = []
    for request in requests:
        size, amount = request
        for i in range(k):
            if table_capacities[i] >= size:
                table_capacities[i] -= size
                total_earned += amount
                accepted_requests.append((amount, i + 1))
                break

    print(f"{len(accepted_requests)} {total_earned}")
    for request in accepted_requests:
        print(*request)

solve()
