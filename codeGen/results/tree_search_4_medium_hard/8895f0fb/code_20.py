import sys

T = int(sys.stdin.readline())  # read the number of test cases

for _ in range(T):
    N = int(sys.stdin.readline())  # read the maximum number of digits in A and B
    dp = [[0] * (N + 1) for _ in range(N + 1)]  # initialize DP table

    for i in range(1, N + 1):  # iterate over each digit in A and B
        for j in range(1, N + 1):
            if i == 0 or j == 0:  # edge case: single-digit numbers
                dp[i][j] = 0
            elif (A := int(str(A)[:i])) + (B := int(str(B)[:j])) < 10:
                dp[i][j] = 1  # no carry
            else:
                if i > 1 and j > 1 and A // 10 + B // 10 >= 10:  # propagate carries from previous pairs
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 1  # new carry

    expected_carries = sum([sum(row) for row in dp]) / (N ** 2)
    print(f"{expected_carries:.6f}")  # output the expected number of non-zero carries
