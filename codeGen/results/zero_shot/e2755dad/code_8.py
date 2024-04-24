def can_be_expressed(n):
    # Check if there exists a k such that (n - 2020*k) is a non-negative integer less than or equal to 2020
    return n % 2020 <= n // 2020

def main():
    t = int(input().strip())  # Read the number of test cases
    for _ in range(t):
        n = int(input().strip())  # Read the value of n for each test case
        print("YES" if can_be_expressed(n) else "NO")

if __name__ == "__main__":
    main()
