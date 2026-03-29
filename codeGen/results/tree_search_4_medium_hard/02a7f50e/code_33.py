def min_destroyed_beacons():
    n = int(input())
    positions = []
    for _ in range(n):
        a, b = map(int, input().split())
        positions.append((a, b))

    dp = [0]
    max_power = 0

    for i in range(1, n+1):
        while len(positions) > 0 and positions[0][0] <= i:
            a, b = positions.pop(0)
            if b <= max_power:
                break
        if len(positions) == 0:
            dp.append(0)
        else:
            a, b = positions[0]
            dp.append(min(len(positions), max_power-b+1))

    return dp[-1]

print(min_destroyed_beacons())
