def can_send_over_network():
    t = int(input())  # number of test cases

    for _ in range(t):
        n = int(input())  # size of sequence b
        b = list(map(int, input().split()))  # sequence b itself

        dp = [[False] * (sum(b) + 1) for _ in range(n+1)]

        for i in range(n+1):
            for j in range(sum(b), -1, -1):  # iterate from right to left
                if i == 0:
                    dp[i][j] = True  # base case: empty sequence a
                elif b[i-1] <= j:
                    dp[i][j] = (dp[i-1][j-b[i-1]] and True) or dp[i][j]
                else:
                    dp[i][j] = False

        if dp[n][sum(b)]:
            print("YES")
        else:
            print("NO")

can_send_over_network()
