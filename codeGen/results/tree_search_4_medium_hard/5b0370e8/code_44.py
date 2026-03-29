import sys

def dfs(i, mask):
    if i == 0: return 1
    ans = 0
    for j in range(k-1, -1, -1):  # Iterate over possible last bits
        new_mask = mask | (1 << j)  # New mask with last bit set
        if ((a[i-1] >> j) & 1):  # If the last bit is 1
            ans += dp[i-1][new_mask >> 1]
        else:
            ans += dp[i-1][mask >> (j+1)]  # or mask >> (j+1)
    return ans

n, k = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0] * (k + 1) for _ in range(n + 1)]

ans = 0
for i in range(1, n + 1):
    and_result = 0
    xor_result = 0
    for j in range(k):
        if ((a[i-1] >> j) & 1):  # If the last bit is 1
            and_result |= (1 << j)
            xor_result ^= (1 << j)
    ans += dfs(i, and_result ^ xor_result)

print(ans % (10**9 + 7))
