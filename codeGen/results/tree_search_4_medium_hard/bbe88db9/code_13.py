import sys; input = lambda: [int(x) for x in input().split()]
n, *ports = input()
dp = [(1, 0, False)]
portals = {1: None}
target_room = n + 1

while dp:
    room, portals_used, ceiling_painted = dp.pop(0)
    
    if room == target_room:
        print(portals_used); sys.exit()

    for portal in (ports[room-1], ports[room-2]):
        new_ceiling_painted = ceiling_painted != (portals.get(room, 1) != portal)
        portals[(room+1) % n] = portal
        dp.append((portal, portals_used + 1, new_ceiling_painted))

print("Not possible")
