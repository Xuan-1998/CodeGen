def solve():
    n = int(input())
    requests = [list(map(int, input().split())) for _ in range(n)]
    requests.sort(key=lambda x: x[1], reverse=True)
    k = int(input())
    table_capacities = [int(input()) for _ in range(k)]

    accepted_requests = []
    total_earned = 0
    allocated_tables = [[] for _ in range(k)]

    for i, (group_size, amount) in enumerate(requests):
        for j, capacity in enumerate(table_capacities):
            if group_size <= capacity:
                accepted_requests.append(i)
                total_earned += amount
                allocated_tables[j].append(group_size)
                table_capacities[j] -= group_size
                break

    print(len(accepted_requests), total_earned)
    for i, request in enumerate(accepted_requests):
        print(request + 1, allocated_tables[0][request].index(min(allocated_tables[0])) + 1)

if __name__ == "__main__":
    solve()
