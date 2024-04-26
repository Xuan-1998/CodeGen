def calculate_factorial():
    t = int(input())  # Read the number of test cases from standard input
    for _ in range(t):
        n = int(input())  # Read the value of n for each test case
        if n < 1:  # Handle edge case where n is less than 1
            print("n must be a positive integer. Please try again.")
            continue
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(factorial)  # Calculate and print the factorial of n

calculate_factorial()
