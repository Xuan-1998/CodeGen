import sys

n = int(sys.stdin.readline())

fares = []
for _ in range(n):
    t = int(sys.stdin.readline())
    minutes_left = t % 60
    if minutes_left <= 1:  # One-trip ticket
        fares.append(20)
    elif minutes_left <= 90:  # 90-minute ticket
        fares.append(50)
    else:  # One-day ticket
        fares.append(120)

print(*fares, sep='\n')
