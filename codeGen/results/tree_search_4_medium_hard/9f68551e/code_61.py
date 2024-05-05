import sys

def min_mana(n, k, h):
    dp = [0] * (max(k) + 1)
    
    for i in range(1, max(k) + 1):
        if not any(j == i for j in k):  # no monsters at the ith second
            dp[i] = dp[i-1]
        else:
            monster_appears = next((j for j in k if j == i), None)
            h_i = h[k.index(monster_appears)]  # health of the monster
            dp[i] = min(max(h_i, dp[i-1]), dp[i-1])
    
    return dp[-1]

# Read input from stdin
n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
h = list(map(int, sys.stdin.readline().split()))

print(min_mana(n, k, h))
