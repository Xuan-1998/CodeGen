max_distribution_index = 0

for _ in range(n):
    # Process nodes one by one based on their degree
    max_distribution_index += dfs(node, parent, labels)

print(max_distribution_index % (10**9 + 7))
