def max_beauty(n, m):
    memo = {(0, p): 0 for p in range(n + 1)}
    memo[(1, p)] = p if p > 0 else 0

    for u, v in sorted([(u, v) for u, v in zip(*[iter([*map(int, open(0).read().split()))][i] for i in [0, 1]]))]:
        t, p = min(v - m + 1, p), max(u - 1, 0)
        memo[(t + 1, p)] = max(memo.get((t, p), 0), (t + 1) * p)

    return max(memo.values())

n, m = map(int, input().split())
print(max_beauty(n, m))
