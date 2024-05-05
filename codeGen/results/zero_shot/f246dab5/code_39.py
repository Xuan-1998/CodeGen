n = int(input())
trip_times = [int(input()) for _ in range(n)]
fare = 0
last_ticket_type = -1

for t in trip_times:
    if last_ticket_type == 0:  # one-trip ticket
        fare += 20
    elif last_ticket_type == 1:  # 90-minute ticket
        if t <= 90:
            fare += 50
        else:
            fare += 50 + (t - 90) * 5
    elif last_ticket_type == 2:  # day-long ticket
        if t <= 1440:
            fare += 120
        else:
            fare += 120 + (t - 1440) * 20

    last_ticket_type = (last_ticket_type + 1) % 3

print(fare)
