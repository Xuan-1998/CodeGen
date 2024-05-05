x, y = map(int, sys.stdin.readline().split())
beacons.append((x, y))
activated = False
destroyed = 0
for i, (a_i, b_i) in enumerate(beacons):
    if not activated:
        activated, destroyed = activate_beacon((a_i, b_i))

print(destroyed)
