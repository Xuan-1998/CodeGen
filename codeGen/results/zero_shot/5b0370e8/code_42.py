def solve():
    t = int(input())
    MOD = 1000000007
    for _ in range(t):
        n, k = map(int, input().split())
        count = 0
        for i in range(2**k):
            and_result = xor_result = 0
            for _ in range(n):
                num = i ^ (_ * (2 ** (k-1)))
                if not (num & (1 << k-1)):
                    and_result ^= num
                else:
                    xor_result ^= num
            if and_result >= xor_result:
                count += 1
        print(count % MOD)

if __name__ == "__main__":
    solve()
