import sys

MOD = 10**9 + 7

dp = [[[0 for _ in range(20)] for _ in range(20)] for _ in range(315)]

def solve():
    a, b = map(int, input().split())
    
    res = 0
    i = 0
    while i <= 314159:
        res = (res + ((a & 1) ^ (b & 1))) % MOD
        a >>= 1
        b >>= 1
        if b == 0: break
        i += 1

    print(res)

if __name__ == "__main__":
    solve()
