import sys

n = int(sys.stdin.readline())

fares = []
for _ in range(n):
    t_i = int(sys.stdin.readline())
    if t_i >= 14400:  # daily ticket
        fares.append(120)
    elif t_i % 90 <= 0:  # 90-minute ticket
        fares.append(50)
    else:  # single-trip ticket
        fares.append(20)

for fare in fares:
    print(fare)
