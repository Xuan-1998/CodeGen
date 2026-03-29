import sys

def solution():
    n = int(sys.stdin.readline())
    p = [int(x) for x in sys.stdin.readline().split()]

    # Initialize a list to keep track of whether we use the first or second portal at each room
    use_first = [True] * (n + 1)

    # Initialize the count of crosses on the ceiling of each room
    cross_count = [0] * (n + 1)

    for i in range(2, n + 1):
        if sum(cross_count[:i]) % 2 == 0:
            use_first[i] = True
        else:
            use_first[i] = False

    # Initialize the total number of rooms visited
    total_rooms_visited = 0

    current_room = 1
    while current_room != n + 1:
        if use_first[current_room]:
            current_room = p[total_rooms_visited]
            total_rooms_visited += 1
        else:
            if cross_count[current_room] % 2 == 1:
                current_room = p[total_rooms_visited]
                total_rooms_visited += 1
            cross_count[current_room] += 1

    print(total_rooms_visited % (10**9 + 7))

solution()
