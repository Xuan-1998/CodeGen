def is_valid_permutation(p):
    n = len(p) // 2
    a = p[:n]
    b = p[n:]
    
    # Check if the first element of 'a' is smaller than the first element of 'b'
    if a[0] >= b[0]:
        return "NO"
    
    # Check if all elements in 'a' are less than all elements in 'b'
    for i, x in enumerate(a):
        if any(x <= y for y in b):
            return "NO"
    
    return "YES"

n = int(input())
p = list(map(int, input().split()))
print(is_valid_permutation(p))
