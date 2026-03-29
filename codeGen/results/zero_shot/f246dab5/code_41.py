# Let's start by breaking down the problem into smaller steps
# Step 1: Understand the rules of the ticketing system
# There are three types of tickets:
#   - One trip costs 20 BYTeland rubles
#   - 90 minutes costs 50 BYTeland rubles
#   - One day (1440 minutes) costs 120 BYTeland rubles

# Step 2: Understand how the system chooses the optimal ticket for each trip
# For each trip, we need to find the minimum cost of the tickets that cover the trip time
# We can use a greedy algorithm to solve this problem

def calculate_fare():
    n = int(input())  # Read the number of trips from stdin
    fares = [0] * n  # Initialize an array to store the fare for each trip

    for i in range(n):
        t_i = int(input())  # Read the time of trip i from stdin
        total_minutes = t_i % 60  # Calculate the remaining minutes of the current hour
        day_tickets = t_i // 1440  # Calculate the number of full days passed
        ninety_minute_tickets = (t_i // 90) - day_tickets * (1440 // 90)  # Calculate the number of 90-minute tickets used
        one_trip_tickets = (total_minutes + 89) // 60  # Calculate the number of one-trip tickets used

        fares[i] = 20 * one_trip_tickets + 50 * ninety_minute_tickets + 120 * day_tickets  # Calculate the total fare for this trip

    # Print the fares to stdout
    for f in fares:
        print(f)

calculate_fare()
