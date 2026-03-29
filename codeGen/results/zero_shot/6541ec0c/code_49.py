def solve(t, n, k, values, edges):
    parent = build_dfs_tree(edges)
    if check_conditions(parent):
        return "YES"
    else:
        return "NO"

t, n, k, values, edges = read_input()
print(solve(t, n, k, values, edges))
