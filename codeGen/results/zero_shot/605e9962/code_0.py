from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(v, graph, colors, dp):
    # Initialize the difference for this vertex (1 for black, -1 for white)
    dp[v][0] = 1 if colors[v] == 'B' else -1
    balanced_subtrees = 0

    # Traverse all children
    for child in graph[v]:
        balanced_subtrees += dfs(child, graph, colors, dp)
        
        # Merge child's DP with current vertex's DP
        for diff in list(dp[child].keys()):
            for curr_diff in list(dp[v].keys()):
                new_diff = diff + curr_diff
                dp[v][new_diff] += dp[child][diff] * dp[v][curr_diff]
                
            # If the subtree rooted at the child is balanced, increment the count
            if diff == 0:
                balanced_subtrees += dp[child][diff]

    return balanced_subtrees

def count_balanced_subtrees(n, parents, colors):
    # Build the graph from the parent array
    graph = defaultdict(list)
    for i in range(2, n + 1):
        graph[parents[i - 2]].append(i)
    
    # Dynamic programming dictionary: dp[vertex][difference] = count
    dp = [defaultdict(int) for _ in range(n + 1)]
    
    # Perform DFS and count balanced subtrees
    result = dfs(1, graph, colors, dp)
    return result

def main():
    # Read number of test cases
    t = int(input())
    for _ in range(t):
        n = int(input())
        parents = list(map(int, input().split()))
        colors = ' ' + input().strip()  # Add a space to make the vertex indexing 1-based
        print(count_balanced_subtrees(n, parents, colors))

if __name__ == "__main__":
    main()
