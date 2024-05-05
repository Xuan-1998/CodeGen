import sys

def calculate_fare(trips):
    fare = 0
    prev_end_time = 0
    for trip in trips:
        if trip - prev_end_time < 90:
            fare += 20
        elif trip - prev_end_time < 1440:
            fare += 50
        else:
            fare += 120
        prev_end_time = trip
    return fare

n = int(sys.stdin.readline())
trips = []
for _ in range(n):
    trips.append(int(sys.stdin.readline()))

fares = [calculate_fare(trips[:i+1]) for i in range(n)]

print("\n".join(map(str, fares)))
