def find_winner():
    T = int(input())  # read number of test cases from stdin
    memo = {}

    for _ in range(T):
        M, X = map(int, input().split())  # read M and X

        dp = {}
        for i in range(X+1):  # initialize DP table
            dp[i] = {}

        winner_idx = 0

        for j in range(1, X+1):
            if j == 1:  # base case: only one player left
                winner_idx = (M-1) % X + 1
            else:
                if j not in memo:
                    memo[j] = dp[i-1][((j+M-2)%X)+1]
                winner_idx = memo[j]

            print(winner_idx, end=' ')  # output the winner index

        print()  # newline for next test case
