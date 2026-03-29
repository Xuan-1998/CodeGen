def f(i, j):
    if i == 1: 
        return j # base case for single group
    if memo.get((i, j)):
        return memo[(i, j)]
    
    min_comp = float('inf')
    for k in range(1, j + 1): 
        comp = f(i - 1, k) + (j - k)
        min_comp = min(min_comp, comp)
    memo[(i, j)] = min_comp
    return min_comp

memo = {}
t, l, r = map(int, input().split())
result = sum((t // 10**i) * f(l + i, r) for i in range(6)) - (l * f(r))
print(result % (1e9 + 7))
