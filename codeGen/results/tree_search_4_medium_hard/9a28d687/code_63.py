import heapq

def min_cost_to_sort_strings():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]
    
    dp = [[0] * n for _ in range(n)]
    prev_s = [''] * n
    
    for i in range(1, n):
        for j in range(i):
            if strings[i] < strings[j]:
                heapq.heappush(prev_s[:i], (costs[j], strings[j]))
                dp[i][j] = costs[j]
                while prev_s[0] and prev_s[0][1] == strings[j]:
                    _, s = heapq.heappop(prev_s)
                    dp[i][j] += 1
            else:
                dp[i][j] = dp[j][i]
    
    return -1 if any(dp[i][n-1] for i in range(n)) else sum(costs)

print(min_cost_to_sort_strings())
