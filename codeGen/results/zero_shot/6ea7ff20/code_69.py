def merge(a, b):
    if not a and not b:
        return []
    elif not a:
        return list(b)
    elif not b:
        return list(a)
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])

n = int(input())
p = list(map(int, input().split()))
if p == merge([i for i in range(1, n+1)], [i for i in range(n, 2*n-1, -1)]):
    print("YES")
else:
    print("NO")
