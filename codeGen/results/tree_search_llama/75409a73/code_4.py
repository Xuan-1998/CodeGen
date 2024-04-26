def calculate_factorial():
    t = int(input())  # read the number of test cases
    for _ in range(t):
        n = int(input())  # read the input integer
        result = 1
        for i in range(2, n+1):
            result *= i
        print(result)

if __name__ == "__main__":
    calculate_factorial()
