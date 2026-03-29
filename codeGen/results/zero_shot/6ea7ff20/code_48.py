def merge(a, b):
    if not a:
        return b
    elif not b:
        return a
    else:
        if a[0] <= b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])

def is_merge_permutation(p):
    n = len(p) // 2
    for i in range(n):
        a = p[:i+1]
        b = p[i+1:]
        if sorted(set(a)) == sorted(set(b)) and set(a).union(set(b)) == set(p):
            return "YES"
    return "NO"

n = int(input())
p = list(map(int, input().split()))
print(is_merge_permutation(p))
