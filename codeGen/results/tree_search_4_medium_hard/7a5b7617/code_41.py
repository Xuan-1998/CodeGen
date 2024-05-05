def calculate_steady_tables():
    t = int(input())
    modulo = 1000000000

    for _ in range(t):
        n, m = map(int, input().split())

        # Create a memoization table to store intermediate results
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base case: The number of ways to fill the first row is 1.
        for j in range(m + 1):
            dp[0][j] = 1

        # Fill up the memoization table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If the current sum is less than or equal to M,
                # calculate the number of ways to fill this cell.
                if dp[i - 1][j] > 0:
                    dp[i][j] = sum(dp[i - 1][k] for k in range(j + 1)) % modulo

        # Calculate the total number of steady tables
        total = 0
        for j in range(m + 1):
            total += dp[n][j]
        print(total % modulo)

calculate_steady_tables()
