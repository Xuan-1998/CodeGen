import sys

# Read input from stdin
n, t = map(int, sys.stdin.readline().split())
fraction = float(sys.stdin.readline())

total_rounding_places = n - 1
max_grade = 0

for i in range(total_rounding_places):
    rounded_fraction = round(fraction, i + 1)
    grade = int(rounded_fraction * (n - i - 1) / (n - 1))
    max_grade = max(max_grade, grade)

# Print the maximum possible grade to stdout
print(max_grade)
