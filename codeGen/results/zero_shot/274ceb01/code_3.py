def min_marks_below_water(n, marks):
    return sum(marks[:i] for i in range(1, n+1))

# Read input from stdin
n = int(input())
marks = list(map(int, input().split()))

# Calculate and print the result
print(min_marks_below_water(n, marks))
