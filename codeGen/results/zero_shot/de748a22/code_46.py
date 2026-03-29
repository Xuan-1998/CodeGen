def process_queries(signs, queries):
    n = len(signs)
    q = len(queries)

    # Initialize prefix sums
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + signs[i]

    # Process each query
    for l, r in queries:
        required_sum = sum(signs[l:r+1])
        
        # Find the minimal number of elements that can be removed to achieve the required sum
        min_elements_removed = abs(required_sum) // 2
        
        print(min_elements_removed)

# Example usage
signs = list(input())
queries = []
for _ in range(int(input())): 
    l, r = map(int, input().split())
    queries.append((l-1, r))
process_queries(signs, queries)
