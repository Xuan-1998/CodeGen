from collections import OrderedDict

n = int(input())  # number of strings
costs = [int(input()) for _ in range(n)]  # cost of reversing each string
strings = [input() for _ in range(n)]  # the strings themselves

dp = [0] * (n + 1)  # dynamic programming table
prev_sorted_strings = OrderedDict()  # keep track of previously sorted strings

for i in range(1, n + 1):
    if i == 1:
        dp[i] = costs[0]
    elif prev_sorted_strings:  # there are previously sorted strings
        min_cost = float('inf')
        for prev_string in prev_sorted_strings:
            index = strings.index(prev_string)
            cost = dp[index] + costs[i - 1]
            if cost < min_cost:
                min_cost = cost
        dp[i] = min_cost
    else:  # no previously sorted strings
        dp[i] = dp[i - 1] + costs[i - 1]

print(dp[n])
