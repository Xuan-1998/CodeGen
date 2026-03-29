def solve(t, l, r):
    # TO DO: implement the function f(n)
    def f(n):
        pass

    result = t * sum(f(i) for i in range(l, r+1)) - l * f(r)
    return result % (10**9 + 7)

t, l, r = map(int, input().split())
print(solve(t, l, r))
