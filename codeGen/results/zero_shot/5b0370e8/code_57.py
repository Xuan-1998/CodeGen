def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_sum = 0
        xor_sum = 2 ** k - 1
        for _ in range(n):
            x = int(input())
            and_sum |= x
            xor_sum ^= x
        print((xor_sum & (xor_sum + 1)) // 2)

solve()
