def count_moves(room_number):
    if room_number == n + 1:
        return 0
    if crossed[room_number - 1] % 2 != 0:
        p = portals[room_number - 1]
    else:
        p = room_number
    return 1 + count_moves(p)

n = int(input())
portals = list(map(int, input().split()))
crossed = [0] * (n + 1)
print(count_moves(1) % 1000000007)
