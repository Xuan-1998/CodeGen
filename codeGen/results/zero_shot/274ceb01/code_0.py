def min_sum_below_water(n, marks):
    total_marks = 0
    for i in range(1, n+1):
        total_marks += (i - len([mark for mark in marks if mark >= i]))
    return total_marks

# Example usage:
n = int(input())  # Read the number of days from stdin
marks = list(map(int, input().split()))  # Read the list of marks from stdin
min_sum = min_sum_below_water(n, marks)
print(min_sum)  # Print the minimum possible sum to stdout
