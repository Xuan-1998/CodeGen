# Read input from stdin
n = int(input())
m = int(input())
set = [int(x) for x in input().split()]

# Call the solution function
result = subset_sum_divisible(set, m)

# Print the result to stdout
print(result)
