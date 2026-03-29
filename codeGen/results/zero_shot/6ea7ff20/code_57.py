import sys

def main():
    n = int(sys.stdin.readline())
    p = [int(x) for x in sys.stdin.readline().split()]

    # try to find a pair of arrays that merge to permutation p
    found = False
    for i in range(n):
        a = p[:i]
        b = p[i:]
        if len(a) + len(b) == 2 * n and set(a).isdisjoint(set(b)):
            # check if merging a and b results in permutation p
            if merge(a, b) == p:
                print("YES")
                found = True
                break

    if not found:
        print("NO")

if __name__ == "__main__":
    main()
