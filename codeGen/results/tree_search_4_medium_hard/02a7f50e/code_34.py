from bisect import bisect_left

n = int(input())
a = []
b = []

for _ in range(n):
    a.append(int(input()))
    b.append(int(input()))

dp = [0] * (n + 1)
sorted_a = sorted((x, i) for i, x in enumerate(a))

for x, i in sorted_a:
    j = bisect_left(sorted_a, (x - 1,))  # find the last position to the left of x
    if j > 0:  # there are beacons to the left of x
        for k in range(j):
            dp[i] = min(dp[k]) + 1

print(max(dp))
