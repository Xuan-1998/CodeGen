import sys

def calculate_fare():
    n = int(sys.stdin.readline())
    fares = []
    
    for _ in range(n):
        t = int(sys.stdin.readline())
        minutes_left_in_day = 1440 - t
        one_trip_tickets = minutes_left_in_day // 60
        one_day_tickets = min(8, one_trip_tickets)  # at most 8 one-day tickets
        
        minutes_left = (minutes_left_in_day % 60)
        
        if minutes_left >= 90:
            minutes_left -= 90
            one_ninety_minutes_ticket = minutes_left // 30
            fares.append((one_trip_tickets + one_ninety_minutes_ticket * 2) * 20 + one_day_tickets * 120)
        elif minutes_left > 0:
            one_fifty_minutes_tickets = minutes_left // 50
            fares.append((one_trip_tickets + one_ninety_minutes_ticket * 2) * 20 + one_day_tickets * 120 + one_fifty_minutes_tickets * 50)
        else:
            fares.append(one_trip_tickets * 20 + one_day_tickets * 120)
    
    for fare in fares:
        print(fare)

if __name__ == "__main__":
    calculate_fare()
