def merge(a, b):
    if not a:
        return b
    if not b:
        return a

    a_1 = a[0]
    b_1 = b[0]

    if a_1 < b_1:
        return [a_1] + merge(a[1:], b)
    else:
        return [b_1] + merge(a, b[1:])

def validate_permutation(p):
    n = len(p) // 2

    a = []
    b = []

    for i in range(n):
        if p[i] < p[n + i]:
            a.append(p[i])
            b.append(p[n + i])
        else:
            a.append(p[n + i])
            b.append(p[i])

    return True

def main():
    n = int(input())
    p = list(map(int, input().split()))

    if validate_permutation(p):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
