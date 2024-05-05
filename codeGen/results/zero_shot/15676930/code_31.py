import sys

def hares_feeding(n, a, b, c):
    dp = [[0] * (1 << n) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for state in range(1 << n):  # iterate over all possible states
            if ((state >> (i - 1)) & 1) == 0:  # check if hare at position i is hungry
                dp[i][state] = max(dp[i-1][state], dp[i-1][state^(1<<i)] + a[(state>>i)&1])
            else:
                dp[i][state] = max(dp[i-1][state], dp[i-1][state^(1<<i)] + c[(state>>(i-1))&1])

    return dp[n][-1]

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]
b = [int(x) for x in sys.stdin.readline().split()]
c = [int(x) for x in sys.stdin.readline().split()]

print(hares_feeding(n, a, b, c))
