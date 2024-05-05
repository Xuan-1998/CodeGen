def count_moves(n):
    if n == 1:
        return 0

    p = [int(input()) for _ in range(n - 1)]
    portals = {1: 0}

    def paint_crosses(room, crosses):
        if room in portals:
            return portals[room]

        if crosses % 2 == 0:
            next_room = min(range(1, room + 1), key=lambda x: abs(x - p[room - 1]))
        else:
            next_room = max(range(1, room + 1), key=lambda x: abs(x - p[room - 1]))

        portals[room] = 1 + paint_crosses(next_room, crosses + (room in p))
        return portals[room]

    return paint_crosses(n, 0) % 1000000007
