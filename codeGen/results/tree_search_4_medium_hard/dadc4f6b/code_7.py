def total_brightness(n, stars, c, q, views):
    # Initialize memoization dictionary
    memo = {(0, frozenset()): 0}

    def dp(t, r):
        if (t, r) not in memo:
            s = set(star for star in stars if any(x1 <= x2 <= x2 and y1 <= y2 <= y2 for (x1, y1), (x2, y2) in view)
                                    if star[0] + star[1] * t <= c)
            memo[(t, r)] = sum(s)

        return memo[(t, r)]

    result = []
    for view in views:
        t, x1, y1, x2, y2 = view
        result.append(dp(t, frozenset([(x1, y1), (x2, y2)])))

    return '\n'.join(map(str, result))
