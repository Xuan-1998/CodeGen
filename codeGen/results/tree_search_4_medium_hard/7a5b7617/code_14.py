N, M = map(int, input().split())

def dp(n_rows, prev_sum):
    if n_rows == 1:
        return M
    if memoized.get((n_rows, prev_sum)) is not None:
        return memoized[(n_rows, prev_sum)]
    
    total_ways = 0
    for next_sum in range(prev_sum, M + 1):
        total_ways += dp(n_rows + 1, next_sum)
    
    memoized[(n_rows, prev_sum)] = total_ways % 1000000000
    return memoized[(n_rows, prev_sum)]

memoized = {}
print(dp(1, 0))  # Start with the base case for one row
