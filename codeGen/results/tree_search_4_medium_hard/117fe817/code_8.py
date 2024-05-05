def count_ones(n):
    memo = {0: 0}
    def g(k):
        if k not in memo:
            if k == 0:
                memo[k] = 0
            else:
                memo[k] = k + g(int(k / 10))
        return memo[k]
    total_count = sum(g(i) for i in range(n+1))
    print(total_count)
