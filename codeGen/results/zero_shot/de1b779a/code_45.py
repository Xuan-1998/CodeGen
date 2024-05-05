import heapq

n, m, c0, d0 = map(int, input().split())  # read input
stuffings = []

for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    profit_per_gram = (di - ci) / bi  # calculate profit per gram
    stuffings.append((profit_per_gram, ai))  # store stuffing type and amount

stuffings.sort()  # sort by profit per gram in descending order

max_profit = 0

for profit_per_gram, amount in stuffings:
    # calculate how many buns we can make with this stuffing type
    buns_with_stuffing = min(amount, n // (c0 + ci))
    max_profit += buns_with_stuffing * profit_per_gram

remaining_dough = n - c0
buns_without_stuffing = remaining_dough // c0
max_profit += buns_without_stuffing * d0

print(max_profit)  # print the maximum profit
