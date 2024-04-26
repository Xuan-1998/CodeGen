def calculate_factorial():
    t = int(input())
    for _ in range(t):
        n = int(input())
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(factorial)

calculate_factorial()
