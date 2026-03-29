for t in trips:
    if t <= 60:  # one trip ticket
        last_ticket_type = 0
        last_ticket_time = t
    elif t <= 1050:  # 90 minutes ticket
        if last_ticket_type == 1 and last_ticket_time + 90 > t:
            total_fare += 50
            last_ticket_time = t - 60
            last_ticket_type = 2
        else:
            total_fare += 20
            last_ticket_type = 0
            last_ticket_time = t
    else:  # one day ticket
        if last_ticket_type == 2 and last_ticket_time + 1440 > t:
            total_fare += 120
            last_ticket_time = t - 1440
            last_ticket_type = 1
        else:
            total_fare += 50
            last_ticket_type = 1
            last_ticket_time = t - 60

print(total_fare)
