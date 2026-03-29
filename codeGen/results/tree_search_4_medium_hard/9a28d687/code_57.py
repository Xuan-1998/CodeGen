import sys
from collections import defaultdict

def minCostToSortStrings(n, costs, strings):
    dp = [[0] + [float('inf')] * len(max(strings)) for _ in range(n+1)]
    
    # Initialize dp[0][j] to 0 for all j (base case)
    for j in range(len(max(strings))):
        dp[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(len(max(strings))):
            if not strings[i-1][j]:
                dp[i][j] = min([dp[k][j-1] + costs[j-1] + (k==i) for k in range(i+1)])
    
    # Return the minimum total cost required to sort the strings
    return dp[n][len(max(strings)) - 1]

if __name__ == "__main__":
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]
    print(minCostToSortStrings(n, costs, strings))
