import sys

def solve():
    n = int(sys.stdin.readline())
    trips = []
    for _ in range(n):
        trips.append(int(sys.stdin.readline()))

    trips.sort()

    min_cost = 0
    last_used_ticket_time = -1

    fares = [0]
    for t in trips:
        if t - last_used_ticket_time >= 90:
            # Use the 90-minute ticket
            min_cost += 50
            last_used_ticket_time = t + 89
        elif t - last_used_ticket_time >= 14:
            # Use the one-day ticket
            min_cost += 120
            last_used_ticket_time = t + 1439
        else:
            # Use the single-trip ticket
            min_cost += 20

        fares.append(min_cost)

    for fare in fares:
        print(fare, end=' ')
    print()

if __name__ == "__main__":
    solve()
