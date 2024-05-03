import sys

def solve(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        species_count = {}
        for j in range(i):  # Consider previous plants
            species = int(input()) - 1  # Subtract 1 since indexing starts at 0
            species_count[species] = species_count.get(species, 0) + 1

        for j in range(1, m + 1):
            cost = sys.maxsize
            for s in range(m):  # Try each section
                if species_count.get(s, 0) > 0:
                    cost = min(cost, abs(s - int(input()) % m))  # Calculate the cost
                    break

            dp[i][j] = min(dp[i-1][k] + (cost if k != s else 0) for k in range(m))

    return dp[n][m]

n, m = map(int, input().split())
print(solve(n, m))
