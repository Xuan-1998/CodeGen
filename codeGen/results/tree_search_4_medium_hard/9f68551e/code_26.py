def min_mana_required(input):
    n, *k_h = map(int, input().split())
    dp = [float('inf')] * (max(k_h) + 1)
    for i in range(1, n+1):
        j, h = k_h[i-1:i+1]
        dp[j] = min(dp[j-1] + 1, h)
    return dp[-1]

import sys
sys.stdin = open('input.txt', 'r')
print(min_mana_required(sys.stdin.readline()))
