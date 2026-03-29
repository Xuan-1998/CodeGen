def solution():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_counts = {}
        xor_counts = {}
        max_val = 0
        for _ in range(n):
            num = int(input())
            max_val = max(max_val, num)
            if num & (num - 1):  # is power of 2
                and_counts[num] = and_counts.get(num, 0) + 1
            else:
                xor_counts[num] = xor_counts.get(num, 0) + 1
        and_count = sum(counts.get(max_val, 0) for counts in (and_counts,)) % (10**9 + 7)
        xor_count = sum(counts.get(max_val, 0) for counts in (xor_counts,)) % (10**9 + 7)
        print((and_count - xor_count) % (10**9 + 7))

solution()
