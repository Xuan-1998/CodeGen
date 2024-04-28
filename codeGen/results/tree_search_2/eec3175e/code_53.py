def can_sum_divisible_by_m(n, m, arr):
    memo = [[0] * (m + 1) for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        for j in range(m + 1):
            if i == 0:
                memo[i][j] = 1
            elif j == 0:
                memo[i][j] = 1
            elif arr[i - 1] > j:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = (memo[i - 1][j] or memo[i - 1][j - arr[i - 1]])

    return memo[-1][-1]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(can_sum_divisible_by_m(n, m, arr))
