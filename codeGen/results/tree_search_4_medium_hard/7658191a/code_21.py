def max_score(arr):
    n, k, z = len(arr), k, z

    # Initialize dp table with 0s (no moves or elements processed)
    dp = {(i, j): 0 for i in range(n) for j in range(k+1)}

    for i in range(1, n):
        for j in range(min(i, k)+1):
            if j <= z:
                # Process the current element
                dp[(i, j)] = max(dp[(i-1, j-1)] + arr[i], dp[(i-1, j)])
            else:
                # Don't process the current element (or we're out of moves)
                dp[(i, j)] = dp[(i-1, j)]

    return dp[(n-1, k)]
