def solve(n, q, c):
    dp = [[[c for _ in range(101)] for _ in range(101)] for _ in range(q + 1)]

    for i in range(1, q + 1):
        t, x1, y1, x2, y2 = [int(x) for x in input().split()]
        r = set([(x1, y1), (x2, y2)])
        
        for j in range(i - 1, -1, -1):
            intersection = set()
            for k in r:
                x, y = k
                if x <= x2 and y <= y2:  # Check if the rectangle is fully contained within the current view
                    intersection.add((max(x1, x), max(y1, y)))
            dp[i][r] = c + sum(s for s in range(c) if (x, y) in intersection)

    return dp[q][[]][max(1, 100)]  # Return the final answer

n, q, c = [int(x) for x in input().split()]
print(solve(n, q, c))
