def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    memo = {1: 0, 2: 1}
    def helper(n):
        if n in memo:
            return memo[n]
        if n % 2 == 0:
            memo[n] = helper(n // 2) + (n - n // 2)
        else:
            memo[n] = helper((n + 1) // 2) + 1
        return memo[n]
    return helper(n)

def solve(t, l, r):
    res = 0
    for i in range(l, r+1):
        res += t * f(i)
    return res % (10**9 + 7)

# Example usage:
t, l, r = map(int, input().split())
print(solve(t, l, r))
