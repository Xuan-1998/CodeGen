import sys

def merge(a, b):
    if not a:
        return list(b)
    if not b:
        return list(a)
    
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def valid_permutation(p):
    n = len(p) // 2
    a = []
    b = []

    for i in range(len(p)):
        if i % 2 == 0:
            if p[i] < p[i+1]:
                a.append(p[i])
            else:
                b.append(p[i])
        else:
            if p[i-1] < p[i]:
                a.append(p[i])
            else:
                b.append(p[i])

    while len(a) > 1 and a[0] <= a[1]:
        a = [a[0]] + merge(a[1:], [])
    while len(b) > 1 and b[0] <= b[1]:
        b = [b[0]] + merge([], b[1:])

    return set(a).isdisjoint(set(b))

def main():
    n = int(input())
    p = list(map(int, input().split()))
    
    unique_permutations = set(tuple(p[:i]) + tuple(p[i:]) for i in range(1, len(p)))
    
    for permutation in unique_permutations:
        if valid_permutation(permutation):
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    main()
