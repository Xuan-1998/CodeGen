def solve():
    a, b = map(int, input().split())
    dp = [0]
    mod = 10**9 + 7

    for i in range(1, 316):
        dp.append((dp[-1] + ((a & 1) ^ (b >> 1)) % mod) % mod)
        a >>= 1
        b >>= 1

    print(sum(dp) % mod)

if __name__ == "__main__":
    solve()
