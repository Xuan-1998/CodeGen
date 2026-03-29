code = """
import sys

def can_jump(jumps):
    dp = {0: True}
    for i in range(len(jumps) - 1, -1, -1):
        if i > 0 and jumps[i] >= i:
            dp[i] = True
        elif any(dp.get(j) and j + jumps[j] >= i for j in range(i)):
            dp[i] = True
    return dp.get(len(jumps) - 1, False)

jumps = list(map(int, input().split()))
print(can_jump(jumps))
"""
