import sys

n = int(sys.stdin.readline())
fares = []

for _ in range(n):
    t = int(sys.stdin.readline())
    fare = 0
    
    if t <= 89:  # One-trip ticket
        fare = 20
    elif t <= 1439:  # 90-minute ticket + additional 1-trip tickets
        fare += 50
        remaining_time = t - 90
        while remaining_time >= 1:
            fare += 20
            remaining_time -= 1
    else:  # One-day ticket
        fare = 120
    
    fares.append(fare)

for fare in fares:
    print(fare)
