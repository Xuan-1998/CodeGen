def min_operations_to_beautify(s, queries):
    # Function to calculate the cost for a single query
    def cost_to_beautify(l, r):
        cost = 0
        for i in range(l, r):
            # Check for palindrome of length 2
            if s[i] == s[i+1]:
                cost += 1
            # Check for palindrome of length 3
            elif i+2 <= r and s[i] == s[i+2]:
                cost += 1
        return cost
    
    results = []
    for l, r in queries:
        results.append(cost_to_beautify(l-1, r-1))  # Convert to 0-based index
    return results

# Read input from stdin
n, m = map(int, input().split())
s = input()
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Get the minimum operations and print the results
results = min_operations_to_beautify(s, queries)
for result in results:
    print(result)
