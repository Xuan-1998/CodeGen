import sys

def solve():
    t = int(input())
    mod = 10**9 + 7

    for _ in range(t):
        n, k = map(int, input().split())
        and_count = [0] * (2**k)
        xor_count = [0] * (2**k)

        for _ in range(n):
            x = int(input())
            and_count[x] += 1
            xor_count[x ^ ((1 << k) - 1)] += 1

        total_and = sum(1 << i for i, count in enumerate(and_count) if count)
        total_xor = sum(1 << i for i, count in enumerate(xor_count) if count)

        and_count = [(1 << i) for i, count in enumerate(and_count) if count]
        xor_count = [(1 << i) for i, count in enumerate(xor_count) if count]

        count = 0
        for bit in range(k):
            count += (and_count[bit] * and_count[k - 1 - bit]) % mod
            count += (xor_count[bit] * xor_count[k - 1 - bit]) % mod

        print(count % mod)

if __name__ == "__main__":
    solve()
