def can_be_expressed(n):
    # Iterate over all possible values of y
    for y in range(2021):
        if (n - y) % 2020 == 0:
            return "YES"
    return "NO"

def main():
    t = int(input().strip())  # Read the number of test cases
    for _ in range(t):
        n = int(input().strip())  # Read the integer n for each test case
        print(can_be_expressed(n))  # Print the result for each test case

if __name__ == "__main__":
    main()
