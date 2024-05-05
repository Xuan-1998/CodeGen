def solve(n, m):
    # Create a dictionary to store memoized values
    dp = {(i, 0) for i in range(n+1)}

    def dfs(i, j):
        if (i, j) in dp:
            return dp[(i, j)]

        beauty = 0
        if i < n:  # not reached maximum tail length
            for v in range(1, m+1):  # iterate over all vertices
                if v not in [u-1 for u in range(1, i+1)]:  # vertex not in tail
                    beauty = max(beauty, dfs(i+1, j+1) + (i+1)*j)
            dp[(i, j)] = beauty
        else:
            dp[(i, j)] = j  # reached maximum tail length, just count spines

        return beauty

    return max(dfs(0, 0), key=lambda x: x[1])
