def can_be_expressed(n):
    # Iterate over possible values of y
    for y in range(2021):
        # Check if (n - 2021*y) is divisible by 2020
        if (n - 2021 * y) % 2020 == 0:
            return "YES"
    return "NO"

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    print(can_be_expressed(n))
