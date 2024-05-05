def alien_words(n, m):
    memo = {}

    def f(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if j == 0:
            return 1
        
        if 2 * i <= n:
            res = (n-1) * f(1, j-1)
        else:
            res = 2 * f(i+1, j-1)
        
        memo[(i, j)] = res
        return res

    total_words = 0
    for _ in range(m):
        if n % 2 == 0:
            total_words += (n // 2) * (f(1, m) - f(n//2+1, m))
        else:
            total_words += f(1, m)
    
    return total_words % (10**8 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(alien_words(n, m))
