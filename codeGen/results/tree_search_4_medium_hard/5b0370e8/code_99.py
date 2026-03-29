def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (1 << k) for _ in range(n + 1)]
        ans = 0

        for i in range(1, n + 1):
            and_val = x = 0
            for j in range(i):
                bit = int(input())  # input elements
                x ^= bit
                and_val &= bit
            if (x & and_val) >= ((x ^ and_val)):
                ans += 1

        print(ans % (10**9 + 7))

solve()
