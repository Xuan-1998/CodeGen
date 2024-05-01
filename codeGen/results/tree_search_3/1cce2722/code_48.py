from collections import defaultdict

def max_points(a):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    memo = defaultdict(int)

    def dp_func(i, k):
        if i == 0:
            return k * (k - 1) // 2
        if (i, k) in memo:
            return memo[(i, k)]

        if k > 0 and a[i] % 2 != 0:
            delete = dp_func(i - 1, k - 1) + k
        else:
            delete = dp_func(i - 1, k)

        not_delete = dp_func(i - 1, k)
        memo[(i, k)] = max(delete, not_delete)
        return memo[(i, k)]

    return dp_func(n - 1, n // 2)

n = int(input())
a = [int(x) for x in input().split()]
print(max_points(a))
