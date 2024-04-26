def find_min_operations(s, queries):
    operations = []
    for l, r in queries:
        ops = 0
        i = l
        while i < r:
            # Check for palindrome of length 2
            if s[i] == s[i+1]:
                ops += 1
                i += 2
            # Check for palindrome of length 3
            elif i+2 < r and s[i] == s[i+2]:
                ops += 1
                i += 3
            else:
                i += 1
        operations.append(ops)
    return operations

# Read input from stdin
n, m = map(int, input().split())
s = input()
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and output the result
min_operations = find_min_operations(s, queries)
for ops in min_operations:
    print(ops)
