from sys import stdin
def solve():
    m = int(stdin.readline())
    n = int(stdin.readline())
    plants = []
    for _ in range(n):
        s, x = map(int, stdin.readline().split())
        plants.append((s-1, x))
    plants.sort(key=lambda p: p[1])
    dp = [[0] * (m+1) for _ in range(m+1)]
    for i, (s, _) in enumerate(plants):
        j = s - 1
        leftmost_x_of_s = sum(plant[1] for k, plant in enumerate(plants) if k < i and plant[0] == j)
        dp[i][j] = min(dp[max(i-1, 0)][k] + (plants[k][1] - leftmost_x_of_s) for k in range(j+1))
    return int(dp[-1][-1])

print(solve())
