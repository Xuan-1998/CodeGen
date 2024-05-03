def min_replanting_cost(n, m):
    memo = {(i, j): float('inf') for i in range(m+1) for j in range(n+1)}
    memo[(0, 0)] = 0

    for i in range(1, n+1):
        for j in range(1, min(i+1, m)+1):
            if j == 1:
                cost_to_place_in_existing_section = float('inf')
            else:
                cost_to_place_in_existing_section = memo[(j-1, i-1)]
            cost_to_create_new_section = memo[(j-1, i-j)] + j
            memo[(j, i)] = min(cost_to_place_in_existing_section, cost_to_create_new_section)

    return memo[(m, n)]

# Example usage:
n, m = map(int, input().split())
print(min_replanting_cost(n, m))
