def calculate_expression(t, l, r):
    expression = 0
    for i in range(l, r + 1):
        expression += t[i - l] * f(i)
    expression -= l * f(r)
    return expression % (10**9 + 7)

t, l, r = map(int, input().split())
print(calculate_expression(t, l, r))
