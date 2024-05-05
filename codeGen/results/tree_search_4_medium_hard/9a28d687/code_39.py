def minCostToSortStrings():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]

    dp = [[[False] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
    
    max_length = 0
    for i in range(n):
        length = len(strings[i])
        if length > max_length:
            max_length = length
    
    for i in range(1, n+1):
        for k in range(1, n+1):
            dp[i][k] = True
            for j in range(k-1, -1, -1):
                if strings[j-1] > strings[k-1]:
                    break
                else:
                    j -= 1
            if j >= 0 and costs[j] + i <= k:
                dp[i][k] &= dp[i-1][j]
    
    if not dp[n][n]:
        return -1
    else:
        total_cost = sum(costs)
        for i in range(n):
            length = len(strings[i])
            j = n - 1
            while strings[j].startswith(strings[i]):
                j -= 1
            total_cost += costs[j]
        return total_cost

print(minCostToSortStrings())
