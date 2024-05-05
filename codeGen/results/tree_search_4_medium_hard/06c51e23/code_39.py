from math import ceil
from functools import lru_cache

@lru_cache(None)
def max_grade(n, j):
    # Base case: It's always possible to get 0.0 within any time limit.
    if n == 0:
        return 0
    # Calculate the maximum possible grade that can be obtained by rounding the current digit and recursively calculating the maximum possible grade for the remaining time and decimal places.
    round_grade = max_grade(n - 1, j)
    # Calculate the maximum possible grade that can be obtained by not rounding the current digit and recursively calculating the maximum possible grade for the same time and decimal places.
    no_round_grade = max_grade(n, j - ceil((10 ** (n - 1)) * 0.5))
    return max(round_grade, no_round_grade)

# Read input
n, t = map(int, input().split())
# Calculate the maximum possible grade that can be obtained by rounding the decimal fraction within the given time limit.
print(max_grade(n, t))
