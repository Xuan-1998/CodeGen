def calculate_fare():
    n = int(input())
    tickets = {"one-trip": 20, "90-minute": 50, "one-day": 120}
    fares = []
    
    for _ in range(n):
        t = int(input())
        fare = 0
        while True:
            if t <= 0:
                break
            elif t <= 89:
                fare += tickets["one-trip"]
                t -= 1
            elif t <= 1439:
                fare += tickets["90-minute"]
                t -= 90
            else:
                fare += tickets["one-day"]
                t -= 1440
        fares.append(fare)
    
    for fare in fares:
        print(fare)

calculate_fare()
