def merge(a, b):
    if not a and not b:  # both arrays are empty
        return []
    elif not a:  # array a is empty
        return b
    elif not b:  # array b is empty
        return a
    else:
        if a[0] <= b[0]:  # a's first element is smaller or equal to b's first element
            return [a[0]] + merge(a[1:], b)
        else:  # b's first element is larger than a's first element
            return [b[0]] + merge(a, b[1:])

def check_permutation(p):
    n = len(p) // 2  # length of each array
    for i in range(n):
        a = p[i*2:i*2+2]  # elements of array a
        b = p[n*2+i:n*2+(i+1)*2]  # elements of array b
        if merge(a, b) != p:  # permutation doesn't match after merging
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(check_permutation(p))
