def count_arrays(n, k):
    MOD = 10**9 + 7

    # Base case: array with only zeros
    if n == 0:
        return 1 % MOD

    # Recursive case: array with at least one non-zero element
    ans = 0
    for i in range(2**k):
        and_mask = (i >> (k - 1)) & 1
        xor_mask = sum(((j >> (k - 1)) & 1) for j in range(n)) % 2

        if and_mask >= xor_mask:
            ans += count_arrays(n - 1, k)
    return ans % MOD
