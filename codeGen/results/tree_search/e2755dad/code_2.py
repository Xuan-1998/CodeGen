def can_be_expressed(n):
    # Iterate through all possible values of b
    for b in range(n // 2020 + 1):
        if (n - 2021 * b) % 2020 == 0:
            return "YES"
    return "NO"

# Read number of test cases from stdin
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(can_be_expressed(n))
