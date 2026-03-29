def calculate_y(n, sequence):
    memo = {}
    max_depth = 1000

    def helper(x, y, depth):
        if (x, y) in memo:
            return memo[(x, y)]
        if x <= 0 or x > n:
            return -1
        if depth >= max_depth:
            return -1
        next_x = x + sequence[x-1]
        next_y = y + sequence[x-1]
        while next_x > 0 and next_x <= n:
            next_x -= sequence[next_x-1]
            next_y += sequence[next_x-1]
        memo[(x, y)] = next_y
        return helper(next_x, next_y, depth+1)

    for i in range(2, n+1):
        print(helper(i, 0, 0))

