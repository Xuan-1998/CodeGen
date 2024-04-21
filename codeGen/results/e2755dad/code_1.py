def can_be_expressed(n):
    # Check if the remainder of n when divided by 2020 is less than or equal to 2019
    return n % 2020 <= n // 2020

# Read the number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    n = int(input().strip())
    # Output the result for each test case
    print("YES" if can_be_expressed(n) else "NO")
