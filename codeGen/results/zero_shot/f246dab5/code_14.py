import sys

def calculate_fare():
    n = int(sys.stdin.readline())
    fares = []
    
    for _ in range(n):
        t_i = int(sys.stdin.readline())
        
        # Determine which ticket to use based on the time of the trip
        if t_i <= 90:  # one trip ticket
            fare = 20
        elif t_i <= 1530:  # 90 minutes ticket
            fare = 50
        else:  # one day ticket
            fare = 120
        
        fares.append(fare)
    
    print(*fares, sep='\n')

calculate_fare()
