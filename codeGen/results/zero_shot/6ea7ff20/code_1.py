import sys

def merge(a, b):
    if not a and not b:  # both arrays are empty
        return []
    elif not a:  # only array a is empty
        return b
    elif not b:  # only array b is empty
        return a
    else:
        if a[0] < b[0]:  # a_1 < b_1
            return [a[0]] + merge(a[1:], b)
        else:  # a_1 > b_1
            return [b[0]] + merge(a, b[1:])

def find_merge_permutation(n):
    for i in range(2**n):  # generate all possible pairs of arrays
        a = []
        b = []
        for j in range(n):
            if (i >> j) & 1:
                a.append(j)
            else:
                b.append(j)
        p = [x for x in range(2*n)]  # permutation p
        found = True
        while len(a) > 0 and len(b) > 0:  # check if p is a merge of two arrays
            if p[0] < p[n]:  # a_1 < b_1
                a.pop(0)
                p.pop(0)
            elif p[0] > p[n]:
                b.pop(0)
                p.pop(0)
            else:
                found = False
                break
        if not found:  # permutation p is not a merge of two arrays
            print("NO")
            return
    print("YES")

# Read input from stdin
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

# Check if permutation p can be obtained by merging two arrays
find_merge_permutation(n)
