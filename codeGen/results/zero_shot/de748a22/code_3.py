import sys

n, q = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().strip())

queries = []
for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())
    queries.append((l, r))

prefix_sum = [0] * (n + 1)
sign_var_sum = 0
for i in range(n):
    sign_var_sum += arr[i]
    prefix_sum[i + 1] = sign_var_sum

result = 0
for l, r in queries:
    min_remove = float('inf')
    for i in range(l - 1, r):
        sign_var_sum -= arr[i]
        if sign_var_sum == 0:
            min_remove = min(min_remove, i - l + 1)
    result += min_remove

print(result)
