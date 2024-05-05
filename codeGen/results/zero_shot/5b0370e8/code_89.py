def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_count = 0
        xor_count = 0
        for _ in range(n):
            num = int(input())
            and_mask = (1 << k) - 1
            if (num & and_mask) >= xor_result([num] * n):
                and_count += 1
        print((and_count % (10**9 + 7)))
