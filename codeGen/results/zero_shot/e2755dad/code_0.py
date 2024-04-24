def can_be_expressed(n):
    # Since y can't be greater than 2019, we iterate up to 2019
    for y in range(2020):
        # Check if the remaining part is divisible by 2020
        if (n - 2021 * y) % 2020 == 0 and (n - 2021 * y) >= 0:
            return "YES"
    return "NO"

# Read the number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    n = int(input().strip())
    print(can_be_expressed(n))
