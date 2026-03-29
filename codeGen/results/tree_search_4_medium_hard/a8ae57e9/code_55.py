from sys import stdin

n, k, _ = map(int, stdin.readline().split())
requests = [[*map(int, stdin.readline().split())] for _ in range(n)]

state = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if i == 1:
            state[i][j] = max(state[i-1][j], (requests[0][1] <= requests[0][0] and requests[0][0] <= j) * requests[0][1])
        else:
            state[i][j] = max(state[i-1][j], state[i][j-1]) + min(k, requests[i-1][0]) * requests[i-1][1]
            if requests[i-1][1] <= i and requests[i-1][0] <= j:
                state[i][j] = max(state[i][j], requests[i-1][1])

accepted_requests, total_earned = state[-1][-1], state[-1][-1]
print(f"{accepted_requests} {total_earned}")

for i in range(n):
    if accepted_requests > 0 and state[i+1][min(k, requests[i][0])] == state[-1][-1]:
        print(i+1, min(k, requests[i][0]))
