import sys

def count_good_subsequences():
    n = int(input())  # read input
    a = [int(x) for x in input().split()]  # read input array

    dp = [[0] * (10**6 + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, int(a[i]**0.5) + 1):  # iterate up to sqrt(i)
            if a[i] % j == 0:  # if j divides the current number
                dp[i][j] = (dp[i-1][j-1] + 1) % (10**9 + 7)

    return dp[-1][-1]  # return the final count

print(count_good_subsequences())
