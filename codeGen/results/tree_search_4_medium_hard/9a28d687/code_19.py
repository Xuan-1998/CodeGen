code
max_cost = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

dp = [[[0] * (max_cost + 1) for _ in range(len(strings[0]))] for _ in range(n)]
dp[0][j][k] = -1 if j > max_cost else 0

for i in range(1, n):
    for j in range(max_cost):
        dp[i][j][k] = float('inf')
        for prev_strings in range(i):
            diff = len(strings[prev_strings]) - k
            if strings[prev_strings][-diff:] == strings[i][:diff]:
                # String is already in order, just add the cost of reversing it
                dp[i][j][k] = min(dp[i][j][k], dp[prev_strings][j-1][0])
            else:
                # String needs to be reversed or not reversed
                for reverse_cost in range(max_cost - j + 1):
                    if strings[i][:k] < strings[prev_strings][-diff:]:
                        # Reversing the string is cheaper, add its cost and update dp
                        dp[i][j][k] = min(dp[i][j][k], dp[prev_strings][j-1-reverse_cost][0] + costs[i])
                    else:
                        # Not reversing the string is cheaper, just update dp
                        dp[i][j][k] = min(dp[i][j][k], dp[prev_strings][j-1][0])

print(min([dp[n-1][max_cost-j][k] for j in range(max_cost+1) for k in range(len(strings[0]))]))
