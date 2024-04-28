def count_good_sequences():
    n, k = map(int, input().split())
    dp = [0] * (n + 1)
    dp[1] = 1  # Base case: only one way to make a sequence of length 1

    for i in range(2, n + 1):
        dp[i] = sum(1 if j % i == 0 else 0 for j in range(1, i))
        dp[i] %= 1000000007  # Apply modulo

    return dp[n] * (n-1) // (k-1)  # Calculate the number of good sequences
