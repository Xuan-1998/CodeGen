import heapq

def dfs(node, parent):
    if node == -1:
        return 0
    memo = [(0, None)]  # (sum, child)
    for child in children[node]:
        if child != parent:
            sum_child, _ = dfs(child, node)
            memo.append((memo[0][0] + sum_child, child))
    if not memo:
        return 1
    min_sum, _ = heapq.nsmallest(1, memo)[0]
    return min_sum

T = int(input())
for _ in range(T):
    n, *edges = map(int, input().split())
    k = int(input())
    prime_factors = list(map(int, input().split()))
    children = [[] for _ in range(n)]
    for u, v in edges:
        children[u].append(v)
    m = len(prime_factors)
    max_distribution_index = 0
    for u in range(1, n):
        if k % prime_factors[0] == 0:
            sum_u = dfs(u, -1)
            max_distribution_index += sum_u
    print(max_distribution_index % (10**9 + 7))
