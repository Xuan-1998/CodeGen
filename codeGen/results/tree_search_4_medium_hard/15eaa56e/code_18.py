from functools import lru_cache

def solve(table, n, m, k):
    @lru_cache(None)
    def dp(i, j):
        if i > 1 and all(table[i][c] <= table[i-1][c] for c in range(j)):
            return True
        return False

    for l, r in tasks:
        sorted_in_some_column = any(all(dp(l, c) or dp(r, c) for c in range(m)) for _ in range(n))
        if sorted_in_some_column:
            print("Yes")
            return
    print("No")

# Example usage:
n, m = map(int, input().split())  # Get number of rows and columns
table = [list(map(int, input().split())) for _ in range(n)]  # Read the table
k = int(input())  # Get number of tasks
tasks = [[int(x) for x in input().split()] for _ in range(k)]  # Read tasks

solve(table, n, m, k)
