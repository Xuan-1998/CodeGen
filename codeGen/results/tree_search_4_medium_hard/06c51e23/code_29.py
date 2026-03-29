def max_grade(n, t, decimal):
    if t == 0:
        return 0
    
    # Calculate the maximum possible grade for the current prefix
    max_grade_prefix = int(str(decimal)[:n]) + (1 if str(decimal)[n] != '0' else 0)
    
    # Update the time limit and the remaining decimal fraction
    t -= n
    decimal = str(decimal)[n:]
    
    # Recursively call the function with the updated parameters
    return max_grade(t, max_grade_prefix + (1 if decimal[0] != '0' else 0), decimal)

# Read input from stdin
n, t = map(int, input().split())
decimal = float(input())

# Calculate and print the maximum possible grade
print(max_grade(n, t, str(decimal).replace('.', '')))
