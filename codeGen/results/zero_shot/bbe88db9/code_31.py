import sys

def min_portal_moves(n, p):
    current_room = 1
    moves = 0
    for i in range(2, n + 2):
        if (moves % 2) == 1:
            current_room = p[i - 1]
        else:
            current_room += 1
        moves += 1
    return moves

n = int(input())
p = list(map(int, input().split()))
print(min_portal_moves(n, p))
