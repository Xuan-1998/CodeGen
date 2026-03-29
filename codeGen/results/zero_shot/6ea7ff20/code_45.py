import sys

def merge(a, b):
    # implement the merge function as described in the problem statement
    pass  # fill in the implementation later

def check_pair(p, a, b):
    if len(a) + len(b) != len(p):
        return False
    merged = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged == p

def main():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    for _ in range(len(p)):
        # generate all possible pairs of arrays a and b
        for i in range(n):
            for j in range(i+1, 2*n):
                a = p[:i]
                b = p[i:j]
                if check_pair(p, a, b):
                    print("YES")
                    return
    print("NO")

if __name__ == "__main__":
    main()
