c0, d0 = map(int, input().split())
dough_left = c0
max_profit = 0

for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    
    # calculate the maximum number of buns we can make with the i-th stuffing
    buns_with_stuffing = min(n - ci, ai // bi)
    
    # calculate the profit from selling this many buns
    profit_with_stuffing = di * buns_with_stuffing - (bi * buns_with_stuffing + ci * buns_with_stuffing)
    
    # update our maximum profit if this is a better option
    max_profit = max(max_profit, profit_with_stuffing)
    
    # always make as many buns with no stuffing as we like
    buns_without_stuffing = dough_left // c0
    profit_without_stuffing = d0 * buns_without_stuffing - (c0 * buns_without_stuffing)
    
    # update our maximum profit if this is a better option
    max_profit = max(max_profit, profit_without_stuffing)
    
print(max_profit)
