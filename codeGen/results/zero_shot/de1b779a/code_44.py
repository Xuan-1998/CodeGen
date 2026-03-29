n = int(input())
m = int(input())
c0 = int(input())
d0 = int(input())

ai = [int(input()) for _ in range(m)]
bi = [int(input()) for _ in range(m)]
ci = [int(input()) for _ in range(m)]
di = [int(input()) for _ in range(m)]

max_profit = 0
available_dough = c0

for i in range(m):
    stuffing_available = ai[i]
    dough_required = ci[i]
    price = di[i]

    if stuffing_available >= bi[i]:
        profit = (stuffing_available - bi[i]) * price + (dough_required / ci[i]) * d0
    else:
        continue

    max_profit = max(max_profit, profit)
    available_dough -= dough_required

print(max_profit)
