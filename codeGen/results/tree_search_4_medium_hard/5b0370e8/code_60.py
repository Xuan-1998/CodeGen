def count_bitwise_arrays():
    t = int(input())  # Read number of test cases
    MOD = 1e9 + 7

    for _ in range(t):
        n, k = map(int, input().split())  # Read n and k
        xor_result = [0] * (k + 1)
        and_result = [0] * (k + 1)

        for i in range(n):
            x = int(input())  # Read element at index i

            for j in range(k, -1, -1):
                if ((x >> j) & 1):  # If the bit is set
                    xor_result[j] += 1
                    and_result[j] += (1 << j)
                else:
                    xor_result[j] += 2 * xor_result[j + 1]
                    and_result[j] = (and_result[j - 1] >> 1) if j > 0 else 0

        ans = xor_result[k]
        for i in range(k):
            ans += min(xor_result[i], and_result[i])
        print(ans % MOD)

count_bitwise_arrays()
