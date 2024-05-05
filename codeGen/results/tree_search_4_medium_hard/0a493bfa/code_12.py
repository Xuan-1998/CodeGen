def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = set(map(int, input().split()))

    memo = [[0] * (n + 1) for _ in range(n + 1)]

    def beauty(i, j):
        if i == j:
            return 0
        if memo[i][j]:
            return memo[i][j]
        max_beauty = 0
        for k in range(j, -1, -1):
            subset = set(arr[i:k+1])
            if not any(p in subset for p in bad_primes):
                new_beauty = beauty(i, k) + sum(subset)
                max_beauty = max(max_beauty, new_beauty)
        memo[i][j] = max_beauty
        return max_beauty

    print(beauty(0, n-1))
