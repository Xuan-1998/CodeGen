def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_result = 2 ** k - 1
        xor_result = 0
        for _ in range(n):
            x = int(input())
            if (and_result & x) != and_result:
                and_result &= x
            xor_result ^= x
        count = 0
        for i in range(k-1, -1, -1):
            if ((and_result >> i) & 1) == ((xor_result >> i) & 1):
                continue
            mask = (1 << (i+1)) - 1
            count += sum((x >> i) & mask for x in range(2**k))
        print(count % (10**9 + 7))

if __name__ == "__main__":
    solve()
