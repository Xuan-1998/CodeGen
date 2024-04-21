def is_sum_possible(n):
    # Iterate over all possible values of y
    for y in range(n % 2020 + 1):
        if (n - 2021 * y) % 2020 == 0:
            return 'YES'
    return 'NO'

# Read the number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    n = int(input().strip())
    print(is_sum_possible(n))
