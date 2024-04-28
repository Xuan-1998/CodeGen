def factorial(n, memo={}):
    if n == 0 or n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = n * factorial(n-1, memo)
        memo[n] = result
        return result

t = int(input())
for _ in range(t):
    n = int(input())
    print(factorial(n))
