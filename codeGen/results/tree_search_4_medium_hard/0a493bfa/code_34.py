def maxBeauty(a, b):
    n = len(a)
    m = len(b)

    # Initialize dp table with -1 values
    dp = [[-1] * (n + 1) for _ in range(n)]

    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    def beauty(i, j):
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        # Calculate GCD for the current pivot 'a[i]'
        curr_gcd = a[i]
        for k in range(i + 1, j + 1):
            curr_gcd = gcd(curr_gcd, a[k])

        # Apply operations based on the GCD
        beauty_val = 0
        while curr_gcd > 1 and b.count(curr_gcd) == 0:
            if curr_gcd in a[i:j + 1]:
                a[i:j + 1].remove(curr_gcd)
            curr_gcd //= gcd(curr_gcd, max(a[i:j + 1]))

        return beauty(i, j - 1) + sum(x for x in a[i:j + 1] if x == curr_gcd)

    # Calculate maximum beauty for each pivot
    max_beauty = [0]
    for i in range(1, n):
        max_beauty.append(max(beauty(j, i - 1) for j in range(i)))

    return max(max_beauty)
