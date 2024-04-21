def can_form_sum(n):
    # We iterate over the possible values of y
    for y in range((n // 2021) + 1):  # y cannot be larger than n/2021
        if (n - 2021 * y) % 2020 == 0:
            return 'YES'
    return 'NO'

# Read the number of test cases
t = int(input().strip())
for _ in range(t):
    # Read each test case
    n = int(input().strip())
    # Output the result for each test case
    print(can_form_sum(n))
