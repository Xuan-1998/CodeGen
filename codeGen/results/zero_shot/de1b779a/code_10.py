code:
n, m, c0, d0 = map(int, input().split())
max_profit = 0

for _ in range(m):
    a, b, c, d = map(int, input().split())
    
    # calculate the profit for this stuffing type
    stuffed_bun_profit = d - c
    no_stuffing_profit = d0 - c0
    
    if a >= n and b <= a:
        max_profit += (a // (b + 1)) * stuffed_bun_profit
    else:
        max_profit += no_stuffing_profit
        
print(max_profit)
