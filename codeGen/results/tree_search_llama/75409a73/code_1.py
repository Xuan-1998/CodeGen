def calculate_factorial():
    t = int(input())  # Read the number of test cases from stdin
    for _ in range(t):
        n = int(input())  # Read a single integer from stdin
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(factorial)  # Print the calculated factorial to stdout

calculate_factorial()
