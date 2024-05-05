def and_xor_count():
    t = int(input())
    MOD = 10**9 + 7

    dp = {}
    for _ in range(t):
        n, k = map(int, input().split())
        res_and = [0] * (k + 1)
        res_xor = [0] * (k + 1)

        for _ in range(n):
            x = int(input())
            bit = k - 31
            while bit >= 0:
                if not (x & (1 << bit)):
                    break
                bit -= 1

            and_state = 0
            xor_state = 0
            for i in range(bit + 1):
                and_state |= x & (1 << i)
                xor_state ^= x & (1 << i)

            if not res_and[bit]:
                res_and[bit] = dp.get((bit, and_state), 0)
            else:
                res_and[bit] += 1

            if not res_xor[bit]:
                res_xor[bit] = dp.get((bit, xor_state), 0)
            else:
                res_xor[bit] += 1

        count = 0
        for i in range(k + 1):
            if res_and[i] > 0 and (res_xor[i] == 0 or res_xor[i] < res_and[i]):
                count += res_and[i]

        print(count % MOD)
