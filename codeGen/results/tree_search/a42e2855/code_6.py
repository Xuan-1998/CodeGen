def main():
    T = int(input())  # Read the number of test cases
    for _ in range(T):
        N, P = map(int, input().split())  # Read N and P for each test case
        dp = [0.0] * (N+1)
        dp[0] = 1.0  # The probability of being at position 0 is 1

        # Convert P to a probability
        P = P / 100.0
        Q = 1 - P

        # Update the DP array
        for i in range(1, N+1):
            if i - 2 >= 0:
                dp[i] += dp[i-2] * P
            if i - 3 >= 0:
                dp[i] += dp[i-3] * Q

        # Print the answer with exactly 6 digits after the decimal point
        print('{:.6f}'.format(dp[N]))

if __name__ == "__main__":
    main()
