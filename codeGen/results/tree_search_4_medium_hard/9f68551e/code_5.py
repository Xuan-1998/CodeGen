import sys

def min_mana(n):
    k = [int(x) for x in input().split()]
    h = [int(x) for x in input().split()]

    dp = [[0] * n for _ in range(n)]

    # Base case: when all monsters have been killed or the level has ended
    dp[0][0] = 0

    for i in range(1, n):
        for j in range(i+1):
            if k[j] >= i:
                dp[i][j] = min([dp[k-1][k]+h[k-1]-k for k in range(j, i+1)])
            else:
                dp[i][j] = dp[i-k[j]][j]

    # Check if the minimum value is less than 0 (which means it's impossible to kill all monsters)
    for i in range(n):
        for j in range(i+1):
            if dp[i][j] < 0:
                return -1

    return min(dp[-1])

# Read input and print output
t = int(input())

for _ in range(t):
    n = int(input())
    print(min_mana(n))
