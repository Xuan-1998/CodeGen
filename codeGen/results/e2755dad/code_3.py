def can_form_sum(n):
    # We can form the number n by using at most n // 2020 of 2021
    # and the rest with 2020.
    # If n can be formed, the remainder of n when divided by 2020
    # must be less than or equal to the number of 2021s we can use.
    max_2021s = n // 2020
    remainder = n % 2020
    return 'YES' if remainder <= max_2021s else 'NO'

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    result = can_form_sum(n)
    print(result)
