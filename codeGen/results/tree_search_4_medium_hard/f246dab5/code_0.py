def calculate_fare():
    n = int(input())
    fares = []
    
    for _ in range(n):
        t = int(input())
        minutes_left_until_ticket_expires = 1440
        total_cost_so_far = 0
        
        for ticket_type in [(90, 50), (1, 20)]:
            if minutes_left_until_ticket_expires >= ticket_type[0]:
                minutes_left_until_ticket_expires -= ticket_type[0]
                total_cost_so_far += ticket_type[1]
        
        fares.append(total_cost_so_far)
    
    for fare in fares:
        print(fare)

calculate_fare()
