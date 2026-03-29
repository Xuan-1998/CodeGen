import sys

def calculate_fare():
    n = int(sys.stdin.readline().strip())
    
    # Initialize the total fare
    total_fare = 0
    
    # Iterate over each trip
    for _ in range(n):
        t_i = int(sys.stdin.readline().strip())
        
        # Calculate the optimal ticket for this trip
        if t_i < 90:
            fare = 20
        elif t_i <= 1440:
            fare = 50
        else:
            fare = 120
        
        total_fare += fare
        
        print(total_fare)

if __name__ == "__main__":
    calculate_fare()
