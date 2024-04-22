from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent, tree, colors, dp):
    color = 1 if colors[node] == 'W' else -1
    dp[node][offset + color] += 1
    balanced_count = 0

    for child in tree[node]:
        if child != parent:
            balanced_count += dfs(child, node, tree, colors, dp)

            # Combine DP states of child with current node
            for diff in range(-n, n + 1):
                if dp[child][offset + diff] > 0:
                    dp[node][offset + diff + color] += dp[child][offset + diff]
                    if diff + color == 0:
                        balanced_count += dp[child][offset + diff]

            # Reset the DP states for the child to avoid double counting
            for diff in range(-n, n + 1):
                dp[child][offset + diff] = 0

    return balanced_count

def solve(n, parents, colors):
    tree = defaultdict(list)
    for i in range(2, n + 1):
        tree[parents[i - 2]].append(i)
    
    dp = [defaultdict(int) for _ in range(n + 1)]
    global offset
    offset = n  # Offset for indexing into DP array
    
    total_balanced_subtrees = dfs(1, -1, tree, colors, dp)
    return total_balanced_subtrees

def main():
    input_data = sys.stdin.readlines()
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx].strip())
        idx += 1
        parents = list(map(int, input_data[idx].strip().split()))
        idx += 1
        colors = ' ' + input_data[idx].strip()  # Adding a space to make it 1-indexed
        idx += 1
        result = solve(n, parents, colors)
        print(result)

if __name__ == "__main__":
    main()
