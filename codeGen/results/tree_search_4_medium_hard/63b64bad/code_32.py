n = int(input())
a_values = list(map(int, input().split()))
max_y = sum(a_values)
dp = [[-1 for _ in range(max_y + 1)] for _ in range(n + 1)]

def simulate_program(x, y):
    while x <= n and x > 0:
        new_x = x + a_values[x - 1]
        new_y = y + a_values[x - 1]
        dp[new_x][new_y] = new_y
        x, y = new_x, new_y

for i in range(2, n + 1):
    simulate_program(i, 0)

for i in range(n):
    print(dp[i + 1][-1] if dp[i + 1][-1] != -1 else -1)
