def solve():
    t = int(input())
    MOD = 10**9 + 7

    for _ in range(t):
        n, k = map(int, input().split())
        and_count = [0] * (k + 1)
        xor_count = [0] * (k + 1)

        for _ in range(n):
            x = int(input())
            binary_x = format(x, 'b').zfill(k)
            and_count[k - len(binary_x)] += 1
            xor_count[k - len(binary_x)] ^= 1 << len(binary_x) - 1

        and_result = sum((1 << i) * and_count[i] for i in range(k + 1))
        xor_result = sum((1 << i) * xor_count[i] for i in range(k + 1))

        count = (1 << k) - and_result
        result = min(count, xor_result)

        print(result % MOD)
