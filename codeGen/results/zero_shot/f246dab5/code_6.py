import sys

def calculate_fare():
    n = int(sys.stdin.readline())
    fares = []
    for _ in range(n):
        t_i = int(sys.stdin.readline())
        tickets = [0, 50, 120]  # one-trip, 90-minute, day ticket
        fare = 20  # initialize fare with one-trip ticket

        for i, t in enumerate(range(t_i, t_i + 91), start=t_i):
            if i % 1440 == 0:  # reached a new day
                fare += 120
            elif i % 90 == 0:  # reached a new 90-minute interval
                fare += 50

        fares.append(fare)

    for fare in fares:
        print(fare)

calculate_fare()
