def count_ways(A, N):
    mod = 10**9 + 7

    # Initialize dp table with zeros
    dp = [0] * (N + 1)

    # Base case: there is one way to reach sum 0 (i.e., use no elements)
    dp[0] = 1

    for i in range(1, N + 1):
        for num in A:
            if i >= num:
                dp[i] += dp[i - num]
                dp[i] %= mod

    # Count the number of ways to form numbers less than N
    ways_less_than_N = sum(dp[:N])

    # Subtract those counts from the total number of ways to form N
    ways_to_form_N = (1 << 31) - ways_less_than_N

    return ways_to_form_N % mod
