from collections import defaultdict

def memoize(func):
    memo = defaultdict(int)
    def wrapper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        result = func(i, j)
        memo[(i, j)] = result
        return result
    return wrapper

@memoize
def dp(i, j):
    if i > j or (i and dp[i-1][j]):
        return 0
    sum_signs = 0
    for k in range(i, j+1):
        sum_signs += 1 if arr[k] == '+' else -1
    return min((dp[i-1][k-1] + abs(sum_signs)) if k > i and dp[i-1][k-1] else 0 for k in range(i, j+1))

n, q = map(int, input().split())
arr = list(input())
queries = []
for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))

result = [0]
for query in queries:
    l, r = query
    result.append(min(dp(i+1, j) for i, j in zip(range(l, n), range(r, n)) if arr[i] == '+' and arr[j] == '+') + 1)

print('\n'.join(map(str, result)))
