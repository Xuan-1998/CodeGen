def sum_possible(n):
    # Subtract as many 2020s as possible
    remainder = n % 2020
    # Check if the remainder can be covered by 2021s
    return "YES" if remainder <= n // 2020 else "NO"

# Read the number of test cases from stdin
t = int(input().strip())

# Iterate over each test case and print the result
for _ in range(t):
    n = int(input().strip())
    print(sum_possible(n))
