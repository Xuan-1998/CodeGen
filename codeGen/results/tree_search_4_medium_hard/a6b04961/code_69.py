from collections import deque

n, m = map(int, input().split())
dp = [[[0] for _ in range(2)] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    dp[u][1][0] += 1
    dp[v][1][0] += 1

q = deque([(n, 0, 0)])
dp[n][0][0] = n * (m - 1)

while q:
    tail_length, number_of_spines, direction = q.popleft()
    if dp[tail_length][number_of_spines][direction]:
        continue
    for i in range(m):
        u, v = map(int, input().split())
        if u == tail_length and dp[u][number_of_spines][0] > 0:
            new_tail_length = v
            new_number_of_spines = number_of_spines + 1
            q.append((new_tail_length, new_number_of_spines, 1))
        elif v == tail_length and dp[v][number_of_spines][1] > 0:
            new_tail_length = u
            new_number_of_spines = number_of_spines + 1
            q.append((new_tail_length, new_number_of_spines, 0))

print(max(dp[i][j][k] for i in range(n, 0, -1) for j in range(2) for k in (0, 1)))
