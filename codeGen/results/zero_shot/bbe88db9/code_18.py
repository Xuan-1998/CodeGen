def portal_moves(room):
    if room == n + 1:
        return 0
    else:
        if crosses % 2 != 0:  # Check parity of number of crosses
            return 1 + portal_moves(portals[room])
        else:
            return 1 + portal_moves(portals[room])

n = int(input())
portals = {}
crosses = 0
rooms = list(range(1, n + 2))

for i in range(n + 1):
    portals[i] = int(input())

result = portal_moves(1)
print(result % 1000000007)  # Print the answer modulo 10^9 + 7
