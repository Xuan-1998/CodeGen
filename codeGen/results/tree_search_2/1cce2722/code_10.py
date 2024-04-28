def solve():
    n = int(input())
    a = list(map(int, input().split()))
    memo = {}

    def dp(i):
        if i < 0:
            return 0
        if (i,) in memo:
            return memo[(i,)]
        if i >= n:
            return 1

        include = a[i] + dp(i - 2) if i >= 2 else 0
        exclude = dp(i - 1)
        result = max(include, exclude)
        memo[(i,)] = result
        return result

    print(dp(n - 1))

solve()
