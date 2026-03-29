from collections import defaultdict

def simulate_sequence(n, a):
    dp = [[-1 for _ in range(max(a)+2)] for _ in range(n+1)]
    dp[0][0] = 0

    for x in range(1, n+1):
        for y in range(max(a)+1):
            if x > n or x <= 0:
                dp[x][y] = -1
            else:
                new_x = max(x-a[x-1], 0)
                new_y = y + a[x-1]
                dp[x][y] = [new_x, new_y]

    return dp[n][0]

n = int(input())
a = list(map(int, input().split()))
print(simulate_sequence(n, a))
