import sys

def calculate_fare(trips):
    fare = 0
    for t in trips:
        if t <= 90:  # within 90 minutes, use 50 BYR ticket
            fare += 50
        elif t <= 1400:  # within 14 hours, use daily ticket (120 BYR)
            fare += 120
        else:  # single-trip ticket (20 BYR) for all other cases
            fare += 20
    return fare

n = int(sys.stdin.readline())
trips = []
for _ in range(n):
    trips.append(int(sys.stdin.readline()))
sys.stdout.write('\n'.join(map(str, [calculate_fare(trips)])))
