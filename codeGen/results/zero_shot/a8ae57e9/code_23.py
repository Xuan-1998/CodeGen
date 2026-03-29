import heapq
n, k = map(int, input().split())
requests = []
for _ in range(n):
    group_size, total_spend = map(int, input().split())
    requests.append((-total_spend, -group_size))
requests.sort()
tables = [int(input()) for _ in range(k)]
table_capacities = []
for i in range(k):
    table_capacity = int(input())
    table_capacities.append(table_capacity)
available_tables = [(0, i) for i in range(k)]

accepted_requests = 0
total_earned = 0

for request in requests:
    total_spend, group_size = -request[0], -request[1]
    while available_tables and (available_tables[0][0] < group_size or not table_capacities[available_tables[0][1]] >= group_size):
        heapq.heappop(available_tables)
    if available_tables:
        table_capacity, table_index = heapq.heappop(available_tables)
        table_capacities[table_index] -= group_size
        accepted_requests += 1
        total_earned += total_spend

print(accepted_requests, total_earned)

for i in range(accepted_requests):
    print(i+1, requests[i][0])
