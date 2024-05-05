n = int(input())
fares = []
for t in range(n):
    trips_left = 10**9 - t
    if trips_left >= 60:
        fares.append(50)  # use 90-minute ticket
    elif trips_left >= 1:
        fares.append(20)  # use one-trip ticket
    else:
        fares.append(120)  # use one-day ticket

print(*fares, sep='\n')
