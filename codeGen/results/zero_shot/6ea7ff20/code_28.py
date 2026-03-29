import sys

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def can_split_permutation(n, p):
    for i in range(2 * n):
        # Try to split the permutation at this index
        a = p[:i]
        b = p[i:]
        if len(a) == n and len(b) == n and set(a).isdisjoint(set(b)):
            return True
    return False

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        p = [int(x) for x in sys.stdin.readline().split()]
        if can_split_permutation(n, p):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
