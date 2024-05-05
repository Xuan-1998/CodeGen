n = int(input())  # Read the number of days
marks = list(map(int, input().split()))  # Read the marks strictly above the water on each day

# Calculate minimum possible sum
minimum_sum = sum(marks) - n*(n+1)//2

print(minimum_sum)  # Print the result
