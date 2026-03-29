def solve():
    t = int(input())
    MOD = 10**9 + 7
    for _ in range(t):
        n, k = map(int, input().split())
        count = 0
        for i in range(2**k):
            and_result = i
            xor_result = 0
            for j in range(n):
                and_result &= (i >> j) & ((1 << k) - 1)
                xor_result ^= (i >> j) & ((1 << k) - 1)
            if and_result >= xor_result:
                count += 1
        print(count % MOD)

if __name__ == "__main__":
    solve()
