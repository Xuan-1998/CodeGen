def solution():
    n = int(input())
    p = list(map(int, input().split()))
    
    # Initialize an empty set for each array
    a = set()
    b = set()
    
    # Iterate over the permutation and separate elements into sets a and b
    for i in range(0, n):
        if (i + 1) % 2 == 0:
            a.add(p[i])
        else:
            b.add(p[i])
    
    # Check if the sum of lengths of arrays is equal to the length of permutation
    if len(a) + len(b) != 2 * n:
        return "NO"
    
    # Check if there are any common elements between arrays a and b
    if not (a & b):
        return "YES"
    else:
        return "NO"

print(solution())
