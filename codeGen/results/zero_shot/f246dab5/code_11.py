def calculate_fare():
    n = int(input())
    
    # Initialize total fare
    total_fare = 0
    
    for i in range(n):
        t_i = int(input())  # time of trip i
        
        # Calculate minimum cost for this trip
        if t_i % 1440 < 90:
            # Use ticket for 90 minutes if the trip is within the validity period
            total_fare += 50
        elif t_i % 1440 < 1460:
            # Use ticket for one day if the trip is within the last hour of the day
            total_fare += 120
        else:
            # Use individual tickets for each trip otherwise
            total_fare += (t_i // 60) * 20
        
    print(total_fare)
