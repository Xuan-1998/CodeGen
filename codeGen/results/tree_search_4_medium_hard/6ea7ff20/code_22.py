def solve(n, p):
    # Initialize memoization table
    memo = [[False] * (n + 1) for _ in range(2 * n + 1)]

    def dp(i, j):
        if i < j or i >= 2 * n - 1:
            return False
        if j == 0:
            # Check if remaining elements match array b
            return all(pi > p[i - 1] for pi in p[i:])
        if memo[i][j]:
            return True
        memo[i][j] = True
        for k in range(j):
            if dp(i - 1, k) and all(pi > p[i - 1] for pi in p[i:i + k]):
                return True
        return False

    # Check the top-right corner of the dp array
    if dp(2 * n - 1, n):
        print("YES")
    else:
        print("NO")

# Read input from standard input and solve
n = int(input())
p = list(map(int, input().split()))
solve(n, p)
