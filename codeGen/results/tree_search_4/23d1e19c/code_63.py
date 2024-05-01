def min_max_recompute(vertices, edges, fixed_path):
    n = len(vertices)
    m = len(edges)
    dp = {}

    for v in range(n):
        dp[(v, 0)] = (0, 0)

    for edge in edges:
        u, v = edge
        if v not in dp:
            dp[(v, 1)] = (1, 1)  # No edge from v to t or only one vertex left
        elif v == fixed_path[-1]:  # Reached the end of the fixed path
            continue
        else:
            prev_u = fixed_path.index(v)
            for k in range(2, len(fixed_path) - prev_u):
                dp[(v, k)] = (dp.get((fixed_path[prev_u + k], k - 1))[0] + 1, 
                              max(dp.get((fixed_path[prev_u + k], k - 1))[1], 1))

    return dp[(fixed_path[-1], 0)]
