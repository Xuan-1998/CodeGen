import sys
from collections import defaultdict

def min_replanting(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize the base case when there are no plants
    for i in range(m + 1):
        dp[0][i] = i - 1

    for i in range(1, n + 1):
        species = [0] * (m + 1)
        for j in range(m + 1):
            if i >= m:
                # If there are more plants than sections, 
                # then we can simply place all remaining plants
                # in the last section without replanting anything
                dp[i][j] = dp[i - m][max(0, j - 1)]
                break

            for k in range(m + 1):
                if i > 0:
                    species[k] = sum(species[:k]) 
                else:
                    species[k] = 1

                # Calculate the minimum replanting for this section
                min_replanted = float('inf')
                last_section_species = k - 1 if k > 0 else m
                for l in range(k, -1, -1):
                    if species[l] == 0:
                        continue
                    replanted = dp[i - species[l]][l - 1]
                    min_replanted = min(min_replanted, replanted + (last_section_species != k))

                # Update the state
                dp[i][j] = min(dp[i][j], min_replanted)
            break

    return dp[n][m]

# Read input from stdin and print output to stdout.
n, m = map(int, input().split())
print(min_replanting(n, m))
