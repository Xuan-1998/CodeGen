import sys

def solve():
    n, k, c = map(int, input().split())
    requests = []
    for _ in range(n):
        i, p = map(int, input().split())
        requests.append((i, p))

    # Sort requests by spending per person (descending)
    requests.sort(key=lambda x: x[1] / x[0], reverse=True)

    accepted_requests = 0
    total_earned = 0
    table_allocations = []
    for i, (size, spend) in enumerate(requests):
        if size <= c:
            # Accept the request and allocate a table
            accepted_requests += 1
            total_earned += spend
            table_allocations.append((i, 0))
        else:
            # Decline the request
            pass

    print(accepted_requests, total_earned)
    for i, (request_idx, table_idx) in enumerate(table_allocations):
        print(request_idx, table_idx)

if __name__ == "__main__":
    solve()
