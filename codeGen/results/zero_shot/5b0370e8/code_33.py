import sys
input()

def solve():
    n = int(input())
    k = int(input())
    dp = [0] * (1 << k)
    total_and = 0
    total_xor = 0
    for _ in range(n):
        x = int(input())
        total_and |= x
        total_xor ^= x
    and_mask = total_and
    xor_mask = total_xor
    count = 0
    for i in range(1 << k):
        if (and_mask & i) >= (xor_mask & i):
            count += dp[i - and_mask & i]
        dp[i] = dp[i ^ and_mask] + (i & xor_mask)
    print(count % (10**9 + 7))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
