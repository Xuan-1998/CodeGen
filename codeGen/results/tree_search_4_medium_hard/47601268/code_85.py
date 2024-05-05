def count_without_consecutive_ones(n):
    memo = {0: 1}  # base case: no consecutive ones for i=0

    def dp(k, i):
        if (k, i) in memo:
            return memo[(k, i)]

        if k > 0 and i < n:
            count = dp(0, i) + sum(1 for j in range(i+1) if bin(j).count('1') < 2 and j <= i)
            memo[(k, i)] = count
            return count

        if i == 0:  # base case: no consecutive ones for i=0
            return 1 if not any(1 << i & (j & -j)) for j in range(i+1) else 0

        return 0

    return dp(0, n)
