def count_arrays(nums):
    MOD = 10**9 + 7
    k = len(bin(max(nums))) - 3  # Calculate the number of bits in the maximum number

    dp = [[0] * (k + 1) for _ in range(len(nums) + 1)]

    for i in range(1, len(nums) + 1):
        for j in range(k + 1):
            if j < k:
                and_bit = nums[i - 1] & ((1 << (j + 1)) - 1)
                xor_bit = nums[i - 1] ^ ((1 << (j + 1)) - 1)

                # If the current number has more bits than needed, just consider the last j bits
                if i < len(nums) and j >= k:
                    and_bit &= ((1 << j) - 1)
                    xor_bit ^= ((1 << j) - 1)

                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j]) % MOD

    return sum(dp[-1]) % MOD
