from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(v, graph, colors, dp, results):
    # Base color count for the current node
    color_count = defaultdict(int)
    if colors[v] == 'W':
        color_count[1] = 1
    else:
        color_count[-1] = 1

    # Traverse child subtrees
    for child in graph[v]:
        child_count = dfs(child, graph, colors, dp, results)

        # Combine current subtree counts with child subtree counts
        new_count = defaultdict(int)
        for c1 in color_count:
            for c2 in child_count:
                new_count[c1 + c2] += color_count[c1] * child_count[c2]

        # Update the color count with combined counts
        color_count = new_count

    # Update balanced subtree count
    results[0] += color_count[0]

    # Update DP table
    for diff, count in color_count.items():
        dp[v][diff] += count

    return dp[v]

def solve(test_cases):
    results = []
    for n, parents, colors in test_cases:
        graph = defaultdict(list)
        dp = [defaultdict(int) for _ in range(n + 1)]

        # Construct the tree
        for i, p in enumerate(parents, 2):
            graph[p].append(i)

        # Count balanced subtrees
        result = [0]
        dfs(1, graph, colors, dp, result)
        results.append(result[0])

    return results

def main():
    num_test_cases = int(input())
    test_cases = []
    
    for _ in range(num_test_cases):
        n = int(input())
        parents = list(map(int, input().split()))
        colors = input().strip()
        test_cases.append((n, parents, colors))
    
    results = solve(test_cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
