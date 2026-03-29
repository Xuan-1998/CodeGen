import sys

def read_input():
    n = int(sys.stdin.readline())
    requests = []
    for _ in range(n):
        group_size, amount = map(int, sys.stdin.readline().split())
        requests.append((group_size, amount))
    k = int(sys.stdin.readline())
    max_capacity = int(sys.stdin.readline())
    return requests, k, max_capacity

def solve(requests, k, max_capacity):
    accepted_requests = 0
    total_earned = 0
    table_counts = [0] * (k + 1)
    for group_size, amount in sorted(requests, reverse=True):
        for i in range(k, -1, -1):
            if table_counts[i] + group_size <= max_capacity:
                table_counts[i] += group_size
                accepted_requests += 1
                total_earned += amount
                break

    print(accepted_requests)
    print(total_earned)
    for i, (group_size, _) in enumerate(requests):
        for j in range(k, -1, -1):
            if table_counts[j] + group_size <= max_capacity:
                print(i + 1, j + 1)
                break

requests, k, max_capacity = read_input()
solve(requests, k, max_capacity)
