def max_points(a):
    n = len(a)
    memo = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if a[i - 1] > 105:
            break
        for j in range(i - 2, -1, -1):
            if a[j] > 105:
                break
            memo[i][j] = max(memo[i - 1][j], a[i - 1] + (memo[i - 2][j - 1] if i >= 2 and j >= 1 else 0))
    return memo[n][0]

# Read the input from stdin
n = int(input())
a = list(map(int, input().split()))

print(max_points(a))
