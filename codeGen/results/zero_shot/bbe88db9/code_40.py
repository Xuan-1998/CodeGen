def move(room, direction):
    if direction == "first":
        crosses = room["crosses"]
        if crosses % 2 == 0:
            room["portal"] = room["p_second"]
        else:
            room["portal"] = room["p_first"]
        room["crosses"] += 1
    elif direction == "second":
        room["crosses"] += 1

def min_moves(initial_room, target_room):
    room = {"room_id": initial_room, "crosses": 0, "p_first": None, "p_second": None}
    moves = 0
    while room["room_id"] != target_room:
        if room["room_id"] == 1:  # special case for room 1
            move(room, "first")
        else:
            p_i = [i for i in range(2, room["room_id"]) if p_i[i-1] == room["room_id"]]
            move(room, p_i[0]%2 == 0 and "first" or "second")
        moves += 1
    return moves

n = int(input())
p_i = [int(x) for x in input().split()]
for i in range(2, n+1):
    if p_i[i-1] == i:
        p_i[i-1] = None
print(min_moves(1, n+1) % 1000000007)
