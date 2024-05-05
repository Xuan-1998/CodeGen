python
def calculate_fare():
    n = int(input())
    fares = []
    for _ in range(n):
        trip_time = int(input())
        tickets = 0
        while trip_time >= 60:
            if trip_time >= 1440: 
                ticket_type = "day"
                trip_time -= 1440
            elif trip_time >= 90:
                ticket_type = "90 minutes"
                trip_time -= 90
            else:
                ticket_type = "1 trip"
                trip_time -= 60
            tickets += {"1 trip": 20, "90 minutes": 50, "day": 120}[ticket_type]
        fares.append(tickets + (trip_time // 60))
    for fare in fares:
        print(fare)
