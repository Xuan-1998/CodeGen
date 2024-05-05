from collections import defaultdict

def solve(n, k, max_capacity, requests):
    dp = {0: (0, k, 0)}
    for _, pi in requests:
        ci = next(request[0] for request in requests if request[1] == pi)
        accepted_requests, remaining_tables, max_earned = dp.get(min(max_earned, pi) // ci - 1, (0, k, 0))
        if max_earned + pi > max_earned:
            dp[max_earned + pi] = (accepted_requests + 1, min(remaining_tables - ci, k), max_earned + pi)
    accepted_requests, remaining_tables, max_earned = max(dp.values(), key=lambda x: x[2])
    return accepted_requests, max_earned

n, k, *requests = [int(x) for x in open('input.txt').read().split()]
print(*solve(n, k, next(int(x) for x in open('tables.txt').read().split()), [(ci, pi) for ci, pi in zip(*[list(map(int, line.split())) for line in open('requests.txt')])]), sep='\n')
