code starts here

import sys
n = int(sys.stdin.readline().strip())
requests = []
for _ in range(n):
    request = list(map(int, sys.stdin.readline().split()))
    requests.append(request)

k = int(sys.stdin.readline().strip())
max_capacity = int(sys.stdin.readline().strip())

requests.sort(key=lambda x: (x[1], -x[0]))

total_amount_earned = 0
accepted_requests = []
for i in range(n):
    for j in range(k):
        if requests[i][0] <= max_capacity:
            accepted_requests.append((i+1, j+1))
            total_amount_earned += requests[i][1]
            break

print(len(accepted_requests), total_amount_earned)
for i in range(len(accepted_requests)):
    print(*accepted_requests[i])

code ends here
