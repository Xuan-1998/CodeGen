def solve():
    a, b = map(int, input().split())
    dp = [0]  # Initialize dynamic programming array

    for i in range(1, 316241):
        dp.append((dp[-1] ^ (b << 1)) % (10**9 + 7))

    print(sum(dp) % (10**9 + 7))

if __name__ == "__main__":
    solve()
