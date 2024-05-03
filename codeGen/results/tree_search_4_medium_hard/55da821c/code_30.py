import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    plants = []
    for _ in range(n):
        s, x = map(int, input().split())
        plants.append((s-1, x))

    plants.sort(key=lambda x: x[1])
    dp = [[0] * (m+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(i):
            last_s = 0
            replant_count = 0
            for k, (species, _) in enumerate(plants):
                if species == i:
                    last_s = species
                elif species != last_s and j < len(plants)-k-1:
                    replant_count += 1
                else:
                    break
            dp[i][j] = replant_count + dp[j][i]

    print(min(dp[m]))

solve()
