def count_stable_tables(N, M):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0:  # base case: empty table configuration
            return 1

        if j < 0 or i > N:  # invalid table configuration
            return 0

        if i == N and j > M:  # constraint not met (sum of elements in the Nth row is greater than M)
            return 0

        # consider all possible values for the current cell (i, j)
        total = 0
        for k in range(min(j + 1, M) + 1):
            if i > 0:  # check constraint that sum of elements in ith row is not less than the sum of elements in (i-1)th row
                if k < dp(i - 1, j):  # ensure sum of elements in ith row is at least as large as the sum of elements in (i-1)th row
                    total += 1

        memo[(i, j)] = total
        return total

    result = 0
    for j in range(M + 1):
        result += dp(N, j)
    return result % 1000000000


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(count_stable_tables(N, M))
