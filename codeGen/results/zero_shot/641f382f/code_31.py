import math
from sys import stdin

def main():
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))

    # Initial GCD of the array
    gcd_of_all = arr[0]

    # Find the GCD of the entire array
    for num in arr:
        gcd_of_all = math.gcd(gcd_of_all, num)

    # If the GCD of all elements is 1, we can make all elements 1
    if gcd_of_all == 1:
        print(n - 1)  # Propagate the first 1 to the entire array
    else:
        print(-1)  # It's impossible to make all elements equal to 1

if __name__ == "__main__":
    main()
