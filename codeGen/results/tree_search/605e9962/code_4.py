from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent, tree, colors, dp):
    color = 1 if colors[node] == 'W' else -1
    dp[node][color] += 1
    balanced_subtrees = 0 if color == -1 else 1  # Count the current node if it's white
    
    for child in tree[node]:
        if child != parent:
            balanced_subtrees += dfs(child, node, tree, colors, dp)
            # Merge child's DP states into the parent's while counting balanced subtrees
            for diff in dp[child]:
                dp[node][diff + color] += dp[child][diff]
                if diff + color == 0:
                    balanced_subtrees += dp[child][diff]
                    
    return balanced_subtrees

def count_balanced_subtrees(n, parents, colors):
    tree = defaultdict(list)
    for i in range(2, n + 1):
        tree[parents[i - 2]].append(i)
        tree[i].append(parents[i - 2])
    
    dp = defaultdict(lambda: defaultdict(int))
    result = dfs(1, -1, tree, colors, dp)
    return result

def main():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n = int(input())
        parents = list(map(int, input().split()))
        colors = ' ' + input().strip()  # Add a space to align the indices
        print(count_balanced_subtrees(n, parents, colors))

if __name__ == "__main__":
    main()
