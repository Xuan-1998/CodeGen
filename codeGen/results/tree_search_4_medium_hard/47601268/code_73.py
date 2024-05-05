def count_numbers(n):
    def update_bit(bit_tree, idx, val):
        while idx < len(bit_tree):
            bit_tree[idx] += val
            idx += 1 if not val else 0

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        last_bit = (i & 1) == 1
        if last_bit:
            idx = i - 1
            while idx > 0 and bit_tree[idx]:
                idx -= 1
            dp[i] += dp[idx] * ((bit_tree[idx]) % 2)
        dp[i] += dp[i - 1]
        update_bit(bit_tree, i, last_bit)

    return dp[n]

n = int(input())
print(count_numbers(n))
