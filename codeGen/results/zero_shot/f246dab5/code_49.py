n = int(input())
tickets = [20, 50, 120]
fares = []
for t in range(n):
    trip_time = int(input())
    used_ticket = None
    for ticket in tickets:
        if trip_time <= ticket:
            used_ticket = ticket
            break
    if used_ticket is None:
        used_ticket = tickets[-1]  # use the longest ticket
    fares.append(used_ticket)
print(*fares, sep='\n')
