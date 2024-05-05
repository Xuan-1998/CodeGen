from collections import defaultdict

def calculate_fare(n):
    # Initialize a dictionary to store previously computed values
    dp = defaultdict(int)
    
    # Iterate over the trips and update the minimum cost for each trip
    for i in range(1, n + 1):
        t_i = int(input())  # Read the time of trip i
        
        if i == 1:  # For the first trip, it's a new ticket, so the cost is 20
            dp[i] = 20
        else:
            # Calculate the minimum cost for this trip based on previous trips' costs
            t_i_1 = i - 1
            if t_i_1 % 60 < 90:  # If less than 90 minutes, use a 50-ruble ticket
                dp[i] = min(dp[t_i_1], 20 + (t_i - t_i_1) // 60 * 50)
            else:  # Otherwise, use a 120-ruble ticket
                dp[i] = min(dp[t_i_1], 20 + (t_i - t_i_1) // 60 * 120)
    
    # Print the minimum cost for each trip
    for i in range(1, n + 1):
        print(dp[i])

# Read the number of trips from standard input and call the function
n = int(input())
calculate_fare(n)
