def main():
    # Read the number of days
    n = int(input().strip())
    
    # Read the number of marks above the water level for each day
    marks_above = list(map(int, input().strip().split()))
    
    # Initialize the sum of marks below the water level
    sum_below = 0
    
    # Initialize the highest water level observed so far
    highest = -1
    
    # Iterate over each day
    for i in range(n):
        # Calculate the current water level (marks above + 1)
        current_level = marks_above[i] + 1
        
        # If the current water level is higher than the highest observed,
        # increment the sum of marks below the water level
        if current_level > highest:
            sum_below += i - current_level
            highest = current_level
    
    # Output the result
    print(sum_below)

if __name__ == "__main__":
    main()
