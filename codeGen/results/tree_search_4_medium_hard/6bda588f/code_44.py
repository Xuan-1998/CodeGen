def solve(n, s, memo):
    if (n, 0) in memo:
        return memo[(n, 0)]

    if n == 1:
        return a_n * (a_n - s)

    min_val = float('inf')
    for i in range(a_n + 1):
        x_i = min(i, s)
        y_i = a_n - x_i
        if (n-1, prefix_sum) in memo:
            val = memo[(n-1, prefix_sum)] + x_i * a_n + y_i * s
        else:
            val = solve(n-1, s, {(k, v): k for k, v in memo.items()}) + x_i * a_n + y_i * s
        min_val = min(min_val, val)
    return min_val


t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a_n = list(map(int, input().split()))
    memo = {}
    print(solve(n, s, memo))
