import sys

def read_input():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    return n, p

def is_mergeable(p):
    # Check if the permutation can be merged
    i = 0
    for j in range(len(p)):
        while i < len(p) and p[i] <= p[j]:
            i += 1
        if i > j:
            return False
    return True

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, p = read_input()
        if is_mergeable(p):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
