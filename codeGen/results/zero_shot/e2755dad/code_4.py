def can_be_expressed(n):
    # Iterate through the possible number of 2020s
    for x in range(n // 2020 + 1):
        # Check if the remainder can be expressed using 2021s
        if (n - 2020 * x) % 2021 == 0:
            return "YES"
    return "NO"

# Read the number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    n = int(input().strip())
    result = can_be_expressed(n)
    print(result)
