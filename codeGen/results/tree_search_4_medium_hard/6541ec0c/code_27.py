def solve(n, k, edges):
    # Initialize the memoization table
    memo = [[[0, 10**9] for _ in range(k + 1)] for _ in range(n)]

    def dfs(node, mi, mx, parent, mask):
        if node == -1:
            return True

        # Update the memoization table
        memo[node][mask[0]][mask[1]] = (mi, mx)

        for child in edges[node]:
            if child != parent:
                for new_mask in [(mask[0] + 1, mask[1]), (mask[0], mask[1] + 1)]:
                    # Check if the XOR value of the child node is within the bounds
                    if (memo[child][new_mask[0]][new_mask[1]][0] <= mi and
                            memo[child][new_mask[0]][new_mask[1]][1] >= mx):
                        return dfs(child, min(mi, memo[child][new_mask[0]][new_mask[1]][0]),
                                     max(mx, memo[child][new_mask[0]][new_mask[1]][1]), node, new_mask)

        return False

    # Perform DFS from the root node
    if not dfs(0, 10**9, 0, -1, (0, k)):
        print("NO")
    else:
        print("YES")
