def solve(t, l, r):
    result = 0
    for i in range(t):
        if i < l:
            result += f(i)
        elif i > r:
            break
        else:
            result -= (l - 1) * f(l)
            break

    return result % (10**9 + 7)

t, l, r = map(int, input().split())
print(solve(t, l, r))
