def merge(a, b):
    if not a and b:
        return b
    if a and not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    return [b[0]] + merge(a, b[1:])

def has_common_elements(p):
    n = len(p) // 2
    a = []
    for x in p:
        if not a or x <= a[-1]:
            a.append(x)
        else:
            break
    b = list(set(p) - set(a))
    return any(x in a and x in b for x in a)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = [int(x) for x in input().split()]
        if has_common_elements(p):
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()
