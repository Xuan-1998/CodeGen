def merge(a, b):
    if not a and not b:  # both arrays are empty
        return []
    elif not a:  # only array a is empty
        return b
    elif not b:  # only array b is empty
        return a
    else:
        if a[0] < b[0]:  # first element of a is smaller than first element of b
            return [a[0]] + merge(a[1:], b)
        else:  # first element of a is larger or equal to first element of b
            return [b[0]] + merge(a, b[1:])

def can_form_permutation(p):
    n = len(p) // 2  # length of each array
    for i in range(n):
        if p[i] >= p[n + i]:  # first element of a is larger or equal to first element of b
            return False  # permutation cannot be formed by merging two arrays
    return True  # permutation can be formed by merging two arrays

def solve():
    t = int(input())  # number of test cases
    for _ in range(t):
        n = int(input())  # length of each array
        p = list(map(int, input().split()))  # permutation
        if can_form_permutation(p):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
