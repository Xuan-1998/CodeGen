def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        
        if can_merge(p):
            print("YES")
        else:
            print("NO")

def can_merge(p):
    n = len(p) // 2
    a = []
    b = []

    for i in range(2 * n):
        if i < n:
            a.append(p[i])
        else:
            b.append(p[i])

    return True if merge(set(a), set(b)) == set(p) else False

def merge(a, b):
    if not a and b:
        return b
    elif a and not b:
        return a
    elif a[0] <= b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

if __name__ == "__main__":
    solve()
