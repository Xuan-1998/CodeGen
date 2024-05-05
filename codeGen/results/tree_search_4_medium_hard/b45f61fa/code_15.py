===BEGIN CODE===
from functools import lru_cache

def multiply_matrices(n):
    p = [int(x) for x in input().split()]
    
    @lru_cache(None)
    def f(i, j):
        if i == 0:
            return 0
        elif j == n - 1:
            return 0
        else:
            return min((f(i, k) + f(k+1, j) + p[i]*p[k+1]*p[j]) for k in range(i, j))

    @lru_cache(None)
    def construct_parenthesis(i, j):
        if i == 0:
            return ''
        elif j == n - 1:
            return ''
        else:
            min_mult = float('inf')
            optimal_k = None
            for k in range(i, j):
                mult = f(i, k) + f(k+1, j) + p[i]*p[k+1]*p[j]
                if mult < min_mult:
                    min_mult = mult
                    optimal_k = k
            return '(' + str(i+1) + construct_parenthesis(optimal_k+1, j) + ')' + str(j+1)

    return construct_parenthesis(0, n-2)
