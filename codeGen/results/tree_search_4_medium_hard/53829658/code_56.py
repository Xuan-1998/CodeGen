import sys

n = int(input())
in_degree_dict = {}
max_in_degree = 0
parent_city = [0] * (n + 1)

for i in range(2, n):
    for j in range(i + 1, n):
        if j not in in_degree_dict:
            in_degree_dict[j] = 0
        in_degree_dict[j] += 1
        max_in_degree = max(max_in_degree, in_degree_dict[j])

dp = [0] * (n + 1)
dp[1] = 0

for i in range(2, n):
    for j in range(i + 1, n):
        if in_degree_dict[j] > 0:
            in_degree_dict[j] -= 1
            dp[i] = min(dp[i], dp[j] + (in_degree_dict[j] > 0))
    parent_city[i] = i - 1 if not any(in_degree_dict[k] == 0 for k in range(i)) else max(k for k in range(i) if in_degree_dict[k] == 0)
    dp[i] = min(dp[i], dp[parent_city[i]] + (in_degree_dict[parent_city[i]] > 0))

min_reversed_roads = float('inf')
optimal_capital = -1

for i in range(2, n):
    if dp[i] < min_reversed_roads:
        min_reversed_roads = dp[i]
        optimal_capital = i

print(min_reversed_roads)
print(optimal_capital)
