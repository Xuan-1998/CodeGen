def solve():
    a = int(input(), 2)
    b = int(input(), 2)

    memo = {}
    total = 0

    def f(b, i):
        if (b, i) in memo:
            return memo[(b, i)]

        if b == 0:
            result = 0
        else:
            result = a ^ (b << 1)
            for j in range(10**9 + 7):
                if i >= j and b >> j & 1:
                    result ^= (a >> j) & 1

        memo[(b, i)] = result % (10**9 + 7)
        return result % (10**9 + 7)

    for i in range(314160):
        total += f(b, i)

    print(total % (10**9 + 7))

solve()
