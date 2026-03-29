import sys

def merge(a, b):
    # implement the merge function here
    pass

def is_merge(a, b, p):
    if len(a) == 0:
        return a + b == p
    elif len(b) == 0:
        return a + b == p
    else:
        # compare the first elements of a and b
        if a[0] < b[0]:
            # add the first element to a and recursively call is_merge
            return is_merge(a[1:], [b[0]] + b[1:], p)
        elif a[0] > b[0]:
            # add the first element to b and recursively call is_merge
            return is_merge([a[0]] + a[1:], b[1:], p)
        else:
            # if the first elements are equal, remove them from both arrays
            return is_merge(a[1:], b[1:], p)

def solve(n, p):
    p.sort()
    for i in range(len(p) // 2):
        a = p[:i+1]
        b = p[i+1:]
        if is_merge(a, b, p):
            return "YES"
    return "NO"

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
print(solve(n, p))
