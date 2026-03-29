def minCostToSortStrings():
    n = int(input())
    costs, strings = [], []
    
    for _ in range(n):
        cost = int(input())
        string = input()
        costs.append(cost)
        strings.append(string)

    dp = [0] * (n + 1)
    prev_min_cost = -1

    for i in range(1, n + 1):
        if not strings[i-1].startswith(strings[i-2]):
            dp[i] = min(dp[i-1], costs[i-1]) + dp[i-2]
        else:
            dp[i] = dp[i-1]

        if prev_min_cost != -1 and dp[i] > prev_min_cost:
            return -1
        prev_min_cost = dp[i]

    return dp[-1]


if __name__ == "__main__":
    print(minCostToSortStrings())
