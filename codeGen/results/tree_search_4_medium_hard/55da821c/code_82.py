import sys

def solve():
    n, m = map(int, input().split())
    dp = [0] * (n + 1)
    prev_species = None

    for i in range(1, n):
        curr_species = int(input()) - 1  # subtract 1 because species are 1-indexed
        if curr_species != prev_species:
            # Consider two options: move the current plant to the next available section or keep it in its original section
            min_replants = min(dp[i-1] + (curr_species - prev_species) if prev_species is not None else 0, dp[i-1])
            dp[i] = min_replants
        else:
            dp[i] = dp[i-1]
        prev_species = curr_species

    return dp[-1]

print(solve())
