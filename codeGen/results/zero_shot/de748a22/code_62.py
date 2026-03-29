def solve_queries(signs, queries):
    pos_count, neg_count = preprocess_array(signs)
    for l, r in queries:
        min_remove = calculate_min_remove(pos_count, neg_count, l, r)
        print(min_remove)

# Example usage:
signs = ["+" * 10 + "-" * 5]
queries = [(2, 7), (4, 9), (1, 3)]
solve_queries(signs, queries)  # Output: 3, 2, 1
