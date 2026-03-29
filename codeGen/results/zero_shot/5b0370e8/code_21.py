def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_result = 0
        xor_result = 0
        for _ in range(n):
            num = int(input())
            and_result |= (num & ((1 << k) - 1))
            xor_result ^= num
        print((and_result >= xor_result).count(True) % (10**9 + 7))

if __name__ == '__main__':
    solve()
