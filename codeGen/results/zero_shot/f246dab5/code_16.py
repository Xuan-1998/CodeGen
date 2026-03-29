def calculate_fare():
    n = int(input())  # number of trips
    fares = []
    
    for _ in range(n):
        t_i = int(input())  # time of trip i
        
        # Initialize fares for each type of ticket
        one_trip_ticket = 0
        ninety_minutes_ticket = 0
        one_day_ticket = 0
        
        while True:
            if t_i % 60 >= 14 * 60:  # trip takes more than a day
                one_day_ticket += 1
                t_i %= (14 * 60) + 1  # reset time to the next minute after the day ends
            elif t_i % 90 < 14 * 60:  # trip takes less than or equal to 90 minutes
                ninety_minutes_ticket += 1
                t_i %= 90  # reset time to the remaining minutes in the ticket
            else:  # trip takes exactly one minute
                one_trip_ticket += 1
                break
        
        fare = (one_day_ticket * 120) + (ninety_minutes_ticket * 50) + (one_trip_ticket * 20)
        fares.append(fare)
    
    print(*fares, sep='\n')

calculate_fare()
