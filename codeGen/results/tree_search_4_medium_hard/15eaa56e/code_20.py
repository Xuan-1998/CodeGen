def is_sorted_table(table):
    n, m = len(table), len(table[0])
    dp = {i: 0 for i in range(n)}
    prev_max = [0] * m

    # Initialize the dynamic programming table
    for j in range(m):
        for i in range(n):
            if i > 0 and table[i][j] <= table[i-1][j]:
                dp[i] = max(dp[i], prev_max[j])
            else:
                dp[i] = dp[i-1]
            prev_max[j] = max(prev_max[j], table[i][j])

    # Check if any subtable is sorted
    for task in tasks:
        l, r = task[0]-1, task[1]-1  # Convert to 0-based indexing
        if all(table[i][c] <= table[i+1][c] for i in range(l, r) for c in range(m)):
            return "Yes"
    return "No"


# Example usage:
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
tasks = [[*map(int, input().split())] for _ in range(k)]

print(is_sorted_table(table))
