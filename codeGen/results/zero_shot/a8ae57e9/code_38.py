import sys

def solve():
    n, k = map(int, input().split())
    requests = []
    for _ in range(n):
        group_size, total_amount = map(int, input().split())
        requests.append((group_size, total_amount))

    requests.sort(key=lambda x: x[1], reverse=True)

    accepted_requests = 0
    total_earned = 0

    table_capacity = k

    for request in requests:
        group_size, total_amount = request
        if table_capacity >= group_size:
            accepted_requests += 1
            total_earned += total_amount
            table_capacity -= group_size
        else:
            break

    print(accepted_requests, total_earned)
    for i, request in enumerate(requests[:accepted_requests]):
        group_size, total_amount = request
        table_assignment = (i % k) + 1
        print(f"{group_size} {table_assignment}")

if __name__ == "__main__":
    solve()
