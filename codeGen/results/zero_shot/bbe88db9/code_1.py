n = int(input())
rooms = {}
for i in range(1, n+2):
    p = int(input())
    rooms[i] = {'crosses': 0, 'portal_room': p}

def find_moves(room):
    if room == n+1:
        return 0
    if rooms[room]['crosses'] % 2 == 0:
        next_room = rooms[room]['portal_room']
    else:
        next_room = room + 1
    rooms[next_room]['crosses'] += 1
    return 1 + find_moves(next_room)

print(find_moves(1) % (10**9 + 7))
