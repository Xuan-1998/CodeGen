n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
path = list(map(int, input().split()))

min_recomputation_count, max_recomputation_count = min_max_recomputation(n, m, edges, path)
print(min_recomputation_count, max_recomputation_count)
