import sys

def merge(a, b):
    result = []
    while a and b:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result.extend(a or b)
    return result

def check_permutation(p, n):
    # Sort the permutation in ascending order
    p.sort()
    
    # Check if the sorted permutation can be divided into two arrays a and b, each of length n, such that there are no common elements between them
    for i in range(2*n):
        if (i % 2) == 0:
            a = p[i//2:i//2+n]
        else:
            b = p[i//2:i//2+n]
        if len(set(a).union(set(b))) < 2*n:  # Check if there are no common elements between a and b
            return "YES"
    return "NO"

# Read the input from stdin
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

print(check_permutation(p, n))
