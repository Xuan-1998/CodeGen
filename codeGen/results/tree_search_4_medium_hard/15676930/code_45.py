from functools import lru_cache

def max_total_joy(n):
    @lru_cache(None)
    def dp(i, j, k):
        if i == 0:  # base case: no more hares
            return 0
        if j > 0 and k > 0:  # both adjacent hares are hungry
            return a[i-1] + dp(i-1, j-1, k-1)
        elif j > 0:  # one full adjacent hare
            return b[i-1] + dp(i-1, j-1, k)
        else:  # both adjacent hares are full
            return c[k-1] + dp(i-1, j, k-1)

    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    max_joys = [[0] * (n+1) for _ in range(n+1)]
    for k in range(1, n+1):
        for j in range(min(k, n)+1):
            max_joys[k][j] = dp(k, j, k)
    return max(max_joys[n])

print(max_total_joy(int(input())))
