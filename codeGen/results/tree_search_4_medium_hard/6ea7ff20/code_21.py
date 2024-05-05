from collections import defaultdict

def merge_permutation(n, p):
    memo = defaultdict(bool)
    for i in range(2*n+1):
        if i == 0:
            continue
        j = min(i//2, n)
        if (i-j)%2 == 1:
            j += 1
        if j > 0 and (i-j) < n and p[i-1] >= p[i-j]:
            memo[(i,j)] = True
        else:
            a = p[:i-j]
            b = p[i-j:i]
            if i > j and sorted(a)[0] <= sorted(b)[0]:
                memo[(i,j)] = (a+b) == p[:i]
    return "YES" if memo[(2*n,n)] else "NO"

n_cases = int(input())
for _ in range(n_cases):
    n = int(input())
    p = list(map(int, input().split()))
    print(merge_permutation(n, p))
