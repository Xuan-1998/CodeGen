# Read the number of trips
n = int(input())

# Initialize a dictionary to store the fare for each minute
fare_dict = {}

# Initialize the total fare
total_fare = 0

# Iterate over each trip
for _ in range(n):
    # Read the time of the trip
    t_i = int(input())
    
    # Calculate the minimum fare required for this trip
    min_fare_required = (t_i // 60) * 20 + ((t_i % 60) == 0 and 1 or 20)
    
    # Update the total fare
    total_fare += min_fare_required
    
    # Update the fare dictionary
    for i in range(t_i, t_i + 61):
        if i not in fare_dict:
            fare_dict[i] = min_fare_required
        else:
            fare_dict[i] = min(fare_dict[i], min_fare_required)
    
    # Print the total fare required after this trip
    print(total_fare)
