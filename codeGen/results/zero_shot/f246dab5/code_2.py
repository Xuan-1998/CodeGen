import sys

n = int(sys.stdin.readline())
fares = []

for i in range(n):
    t_i = int(sys.stdin.readline())
    
    if t_i < 20:
        fare = 20
    elif t_i < 50:
        fare = 50
    else:
        fare = 120
    
    fares.append(fare)

for fare in fares:
    print(fare)
