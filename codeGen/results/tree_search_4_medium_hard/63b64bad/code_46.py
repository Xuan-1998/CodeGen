code
n = int(input())
sequence = list(map(int, input().split()))
dp = [-1] * n

def calculate_y(i):
    x, y = i, 0
    while x <= n and x > 0:
        a_value = sequence[x]
        y += a_value
        x += a_value
        if x > n or x <= 0:
            return -1
        y += a_value
        x -= a_value
    return y

for i in range(n-1):
    dp[i] = calculate_y(i)

print(*dp, sep='\n')
