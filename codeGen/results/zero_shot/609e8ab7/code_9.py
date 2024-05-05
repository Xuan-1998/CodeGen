def solve(tree):
    n = tree['n']
    parents = tree['parents']
    ranges = tree['ranges']

    result = 0
    current_range = [0, 10**9]
    for i in range(1, n+1):
        result += dfs(i-1, -1, current_range)
        print(result)

for tree in trees:
    solve(tree)

