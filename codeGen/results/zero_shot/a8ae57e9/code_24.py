k = int(sys.stdin.readline())
tables = [int(sys.stdin.readline()) for _ in range(k)]

accepted_requests = set()
total_earnings = 0

for group_size, spend in requests:
    while accepted_requests and sum(t[1] for t in tables) < group_size * k:
        # decline the request
        break
    if accepted_requests:
        accepted_requests.add((group_size, spend))
        total_earnings += spend

print(len(accepted_requests), total_earnings)

# Output: number of accepted requests and total earnings
for i, (group_size, spend) in enumerate(accepted_requests):
    print(i + 1, group_size)
