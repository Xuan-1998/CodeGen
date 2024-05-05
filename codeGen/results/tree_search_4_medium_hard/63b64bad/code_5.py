def dp(a, n):
    memo = {}
    def helper(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        if x <= 0 or x > n:
            return -1
        new_x = x + a[x]
        new_y = y + a[x]
        result = helper(new_x, new_y)
        if result == -1:
            return -1
        new_x -= a[x]
        new_y += a[x]
        memo[(x, y)] = new_y
        return new_y

    for i in range(2, n+1):
        print(helper(i-1, 0))
