def solve():
    crosses = 0
    room = 1
    count = 0
    while room < n + 1:
        crosses += 1
        room = simulate_moves(room, crosses)
        count += 1
    return count % (10**9 + 7)

print(solve())
