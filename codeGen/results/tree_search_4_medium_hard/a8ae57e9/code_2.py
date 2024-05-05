from sys import stdin

n = int(stdin.readline())
bookings = []
for _ in range(n):
    s, m = map(int, stdin.readline().split())
    bookings.append((s, m))

k = int(stdin.readline())

dp = [[0] * (k + 1) for _ in range(n + 1)]

c = max(map(lambda x: x[0], bookings))

for i in range(1, n + 1):
    dp[i][0] = -float('inf')
    for j in range(1, min(i + 1, k) + 1):
        if bookings[i-1][0] <= c:
            dp[i][j] = max(dp[i-1][j], dp[max(0, i-1-bookings[i-1][0]), j-1] if bookings[i-1][0] <= c else -float('inf')) + bookings[i-1][1]
        else:
            dp[i][j] = -float('inf')

max_earned = max((val for val in dp[n][1:] if val >= 0), default=0)

print(f"{len(accepted_requests)} {max_earned}")

for request, table in accepted_requests:
    print(request, table)
