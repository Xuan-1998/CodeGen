import sys

n = int(sys.stdin.readline())
fares = [0] * n

for i in range(n):
    t_i = int(sys.stdin.readline())
    if t_i < 1:  # one-trip ticket
        fares[i] += 20
    elif t_i <= 90:  # 90-minute ticket
        fares[i] += 50
    else:  # one-day ticket
        fares[i] += 120

for fare in fares:
    print(fare)
