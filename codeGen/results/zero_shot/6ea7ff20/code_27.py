def solve(n, p):
    p = preprocess_p(p)

    for i in range(len(p)):
        a = p[:i]
        b = p[i:]
        if merge(a, b) == p:
            return "YES"
    return "NO"

# Read input from stdin
n = int(input())
p = list(map(int, input().split()))

print(solve(n, p))
