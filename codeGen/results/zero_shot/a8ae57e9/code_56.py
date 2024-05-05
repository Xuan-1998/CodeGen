import sys

n = int(sys.stdin.readline())
requests = [list(map(int, input().split())) for _ in range(n)]
k = int(sys.stdin.readline())

tables = [[0, 0]] * k
accepted_requests = []
total_earned = 0

requests.sort(key=lambda x: x[1], reverse=True)

for group_size, total_amount in requests:
    for i, table in enumerate(tables):
        if table[1] >= group_size:
            tables[i][1] -= group_size
            accepted_requests.append((group_size, total_amount))
            total_earned += total_amount
            break

print(len(accepted_requests), total_earned)
for i, (group_size, _) in enumerate(accepted_requests):
    print(i+1, group_size)
