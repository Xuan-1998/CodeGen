import sys

def merge(a, b):
    if not a and not b:
        return []
    elif not a:
        return b
    elif not b:
        return a
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])

def check_permutation(n, p):
    left = []
    right = []
    for i in range(2 * n):
        if i < n:
            left.append(p[i])
        else:
            right.append(p[i])

    for i in range(len(left)):
        for j in range(i + 1, len(left)):
            if left[i] > left[j]:
                return "NO"

    for i in range(len(right)):
        for j in range(i + 1, len(right)):
            if right[i] < right[j]:
                return "NO"

    return "YES" if merge(left, right) == p else "NO"

n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().split()]
print(check_permutation(n, p))
