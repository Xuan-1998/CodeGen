def can_be_expressed(n):
    # Find the maximum number of 2020s that can fit into n
    max_2020 = n // 2020
    # Check if the remainder can be made up by 2021s
    remainder = n % 2020
    # If the remainder is less than or equal to the number of 2020s used, we can add that many 2021s instead
    return remainder <= max_2020

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    if can_be_expressed(n):
        print("YES")
    else:
        print("NO")
