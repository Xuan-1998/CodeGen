def solve():
    t = int(input())  # Number of test cases

    for _ in range(t):
        n, m = map(int, input().split())  # Initial number and operations
        dp = [[0] * (m + 1) for _ in range(20)]
        dp2 = [[0] * (m + 1) for _ in range(20)]

        # Base case: one digit is needed initially
        for j in range(m + 1):
            dp[0][j] = 1

        for i in range(1, 20):  # Number of digits
            for j in range(min(i, m) + 1):  # Operations
                if i == 1:  # Edge case: n = 0 or m = 0
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i-1][j] + j) % (10**9 + 7)

        result = dp[-1][-1]
        print(result)
