import sys

def solve():
    a, b = map(int, input().split())
    dp = {0: 0}
    for i in range(1, 316):
        if i & 1:
            dp[i] = (dp.get(i-1, 0) + a) % (10**9+7)
        else:
            dp[i] = dp[i//2]
        b = (b << 1) | (a & 1)
        a >>= 1
    ans = sum((dp[i] + XOR(a, left_shift(b, i))) % (10**9+7) for i in range(316))
    print(ans)

def XOR(a, b):
    return a ^ b

def left_shift(b, i):
    return (b << i)

if __name__ == "__main__":
    solve()
