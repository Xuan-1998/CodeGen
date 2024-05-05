===BEGIN SOLUTION===
# Read input
n, k = map(int, input().split())
requests = [list(map(int, input().split())) for _ in range(n)]
requests.sort()

dp = {(0, 0): (0, 0)}
max_earned = 0

for i, request in enumerate(requests):
    ci, pi = request
    for j in range(k-1, -1, -1):
        if (j, 0) not in dp:
            continue
        state = (dp[(j, 0)][0] + ci * pi, min(dp[(j, 0)][1], k-j))
        if (state[0], j) not in dp:
            dp[state] = state
            max_earned = max(max_earned, state[0])
        else:
            break

# Write output
print(max_earned)
accepted_requests = []
tables_used = []
for state in [(k, 0)] + list(dp.keys()):
    if state[0] > dp[state][0]:
        accepted_requests.append(i+1)
        tables_used.append(min(tables_used[-1]+1, k-state[1]))
    else:
        break

print(len(accepted_requests), max_earned)
for i in range(len(accepted_requests)-1):
    print(accepted_requests[i], tables_used[i])
