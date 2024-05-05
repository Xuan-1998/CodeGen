import sys

def solve():
    n, t = map(int, input().split())
    fraction = float(input())

    # Convert the fraction to string
    fraction_str = str(fraction).lstrip('0').lstrip('.')
    
    # Initialize the maximum grade
    max_grade = 0
    
    # Iterate over all possible rounding positions
    for i in range(n):
        # Calculate the time cost of this rounding position
        time_cost = (i + 1) * t
        
        # Check if we have enough time to round at this position
        if time_cost <= t:
            # Update the maximum grade if necessary
            max_grade = max(max_grade, int(round(10 ** i) * fraction_str.split('.')[1][0]))
    
    print(int(max_grade))

if __name__ == "__main__":
    solve()
