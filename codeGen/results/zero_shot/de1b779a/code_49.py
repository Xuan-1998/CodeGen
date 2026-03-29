import sys

def solve():
    n, m, c0, d0 = map(int, sys.stdin.readline().split())
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    
    max_profit = 0
    remaining_dough = n
    
    for ai, bi, ci, di in a:
        if ci > remaining_dough:
            break
        
        buns = min(remaining_dough // ci, ai // bi)
        profit = buns * di
        max_profit += profit
        remaining_dough -= buns * ci
    
    print(max_profit)

solve()
