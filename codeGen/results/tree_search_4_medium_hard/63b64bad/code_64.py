from collections import defaultdict

n = int(input())
sequence = list(map(int, input().split()))
dp = defaultdict(lambda: [-1] * (10**9 + 1))

def transition(x, y):
    a_x = sequence[x]
    return x - a_x, y + a_x

for i in range(n-1):
    x, y = i+2, 0
    while x > 0 and x <= n:
        if dp[x][y] != -1:
            break
        new_x, new_y = transition(x, y)
        dp[x][y] = [new_x, new_y]
        x, y = new_x, new_y

for i in range(2, n):
    print(dp[i-1][0]) if dp[i-1][0] != -1 else -1
