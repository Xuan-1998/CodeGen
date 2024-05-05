def merge(a, b):
    if not a:
        return b
    if not b:
        return a

    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def is_mergeable(p):
    n = len(p) // 2

    # Check all pairs of elements in increasing order
    for i in range(0, len(p), 2):
        if p[i] > p[i + 1]:
            return False

    return True

def solve():
    n = int(input())
    p = list(map(int, input().split()))

    if is_mergeable(p):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
