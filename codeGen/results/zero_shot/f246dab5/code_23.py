import sys

n = int(sys.stdin.readline())
fares = []

for _ in range(n):
    t_i = int(sys.stdin.readline())
    total_cost = 0
    
    # Calculate the fare for this trip
    if t_i <= 90:  # One-trip ticket
        total_cost += 20
    elif t_i <= 1530:  # 90-minute ticket
        total_cost += 50
    else:  # One-day ticket
        total_cost += 120
    
    fares.append(total_cost)

for fare in fares:
    print(fare)
