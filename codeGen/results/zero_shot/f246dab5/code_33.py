import sys

def min_cost_tickets(trips):
    total_cost = 0
    prev_trip_end = 0
    
    for trip in trips:
        # One-trip ticket (20 BYR)
        if trip - prev_trip_end <= 1:
            total_cost += 20
        # 90-minute ticket (50 BYR)
        elif trip - prev_trip_end <= 90:
            total_cost += 50
        # Day-long ticket (120 BYR)
        else:
            total_cost += 120
        
        prev_trip_end = trip
    
    return total_cost

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    
    trips = []
    for _ in range(n):
        trips.append(int(sys.stdin.readline()))
    
    trips.sort()
    
    print(min_cost_tickets(trips))
