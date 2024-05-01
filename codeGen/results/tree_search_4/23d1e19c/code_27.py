from collections import defaultdict

def min_max_recomputations(n, m, edges, k, fixed_path):
    # Step 1: Initialize dp array with n+1 elements set to negative infinity.
    dp = [-float('inf')] * (n + 1)
    
    # Step 2: Iterate through vertices in the fixed path (from s to t).
    for i in range(k - 1, -1, -1):
        # For each vertex, update dp[i] with the maximum length of the recommended paths between vertices in the fixed path from s to i.
        for j in range(i, k - 1):
            if edges[fixed_path[j] - 1][0] == fixed_path[j]:
                for neighbor in [edge[1] for edge in edges if edge[0] == fixed_path[j]]:
                    dp[i] = max(dp[i], dp[neighbor])
    
    # Calculate max_recomputations and min_recomputations using dp array values.
    max_recomputations = max(dp)
    min_recomputations = dp.index(max(dp))
    
    return max_recomputations, min_recomputations

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [[int(i) for i in line.split()] for line in open("edges.txt", "r")]
    k = int(input())
    fixed_path = [int(i) for i in input().split()]

    max_recomputations, min_recomputations = min_max_recomputations(n, m, edges, k, fixed_path)
    
    print(max_recomputations, min_recomputations)
