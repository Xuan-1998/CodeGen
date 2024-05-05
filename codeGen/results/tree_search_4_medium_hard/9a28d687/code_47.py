from collections import defaultdict

def min_cost_sort(costs, strings):
    max_length = 0
    for s in strings:
        max_length = max(max_length, len(s))
    
    dp = [[0] * (max_length + 1) for _ in range(len(strings) + 1)]
    
    prev_strings = defaultdict(list)
    prev_strings[0].append("")
    for i in range(1, len(strings) + 1):
        prev_strings[i-1].extend(prev_strings[i-2])
        prev_strings[i].sort()
        
    for i in range(1, len(strings) + 1):
        for j in range(max_length + 1):
            if strings[i-1][j:] not in prev_strings[j]:
                dp[i][j] = min(dp[i-1][j-1] + costs[i-1], dp[i-1][j] + costs[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[-1][-1]

# Example usage
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]
print(min_cost_sort(costs, strings))
