def solve():
    MOD = 10**9 + 7

    # Read inputs from standard input
    a = int(input(), 2)
    b = int(input(), 2)

    dp = {}
    result = 0

    for i in range(315):
        if (i, a) not in dp:
            total = (a ^ b) % MOD
            for j in range(i-1, -1, -1):
                total += dp.get((j, b>>1), 0)
            result = (result + total) % MOD
            dp[(i, a)] = result

    print(result)

if __name__ == "__main__":
    solve()
