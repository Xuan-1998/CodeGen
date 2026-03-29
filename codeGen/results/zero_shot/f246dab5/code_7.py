import sys

n = int(sys.stdin.readline())
fares = [0] * n

for i in range(n):
    t_i = int(sys.stdin.readline())
    # Check which ticket to use for this trip
    if t_i < 90:
        fares[i] = 20
    elif t_i < 14400:
        fares[i] = 50
    else:
        fares[i] = 120

print(*fares, sep='\n')
