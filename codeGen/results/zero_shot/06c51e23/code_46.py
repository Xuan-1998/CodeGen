import sys

def maximize_grade(n, t, fraction):
    # Initialize the maximum grade to 0
    max_grade = 0
    
    # Iterate over each digit after the decimal point
    for i in range(1, n+1):
        # Calculate the remaining time and the current digit's value
        remain_time = t - i
        curr_digit = int('0.' + fraction[:-i][::-1][1:] * 10[i-1])
        
        # Round up or down based on the current digit and the remaining time
        if remain_time >= curr_digit:
            max_grade += curr_digit
        else:
            max_grade += remain_time
        
    return round(max_grade)

# Receive inputs from stdin
n, t = map(int, input().split())
fraction = input()

# Calculate and print the maximum grade that can be obtained within the given time limit
print(maximize_grade(n, t, fraction))
