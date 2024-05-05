def read_tree():
    # Read input
    n = int(input())
    tree = []
    for i in range(n):
        parent, left, right = map(int, input().split())
        tree.append([parent, left, right])
    return tree

def max_sum_path(tree):
    # Initialize variables
    max_sum = float('-inf')
    visited = [False] * len(tree)

    def dfs(node, current_sum):
        nonlocal max_sum
        if visited[node]:
            return
        visited[node] = True
        current_sum += tree[node][1]
        if tree[node][2] != -1:
            current_sum += dfs(tree[node][2], current_sum)
        if current_sum > max_sum:
            max_sum = current_sum
        return current_sum

    for i in range(len(tree)):
        if not visited[i]:
            dfs(i, 0)

    return max_sum

tree = read_tree()
print(max_sum_path(tree))
