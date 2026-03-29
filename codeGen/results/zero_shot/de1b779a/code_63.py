n, m, c0, d0 = map(int, input().split())
profit = 0

for i in range(m):
    ai, bi, ci, di = map(int, input().split())
    
    # Calculate the maximum number of buns that can be made with this stuffing
    buns = min(n // ci, bi // c0)
    
    # Calculate the profit from making these buns
    p = (di - bi) * buns
    
    # Add the profit to the total
    profit += p

print(profit)
