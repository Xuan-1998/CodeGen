def f(n):
    if n == 2:  # base case: only two girls left
        return 1
    elif n == 3:  # base case: only three girls left
        return 2
    else:
        # recursive case: sum of f(l) and (r-l+1) times some value
        return f(l) + (r-l+1) * t[f(r)] - l*f(r)

t = [int(x) for x in input().split()]
l, r = map(int, (input().split())[1:])
print((sum(t[i] * f(l+i) for i in range(r-l+1)) - l*f(r)) % (10**9 + 7))
