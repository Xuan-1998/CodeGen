def can_split_permutation(p):
    n = len(p) // 2
    left, right = p[:n], p[n:]
    
    # Check if the two halves have distinct elements
    if set(left) & set(right):
        return "NO"
    
    return "YES"

# Read input from stdin
n = int(input())
p = list(map(int, input().split()))

# Print output to stdout
print(can_split_permutation(p))
