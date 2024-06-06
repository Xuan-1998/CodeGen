import math
import sys

def main():
    n = int(input().strip())
    array = list(map(int, input().strip().split()))

    # Check if there is already a 1 in the array
    if 1 in array:
        print(n - 1)
        return

    # Compute the GCD of all elements
    gcd = array[0]
    for num in array[1:]:
        gcd = math.gcd(gcd, num)

    # If the GCD of all elements is 1, it is possible to make all elements 1
    if gcd == 1:
        print(n - 1)  # The answer is n - 1 because we can make the entire array 1
    else:
        print(-1)  # If the GCD is not 1, it's not possible to make all elements 1

if __name__ == "__main__":
    main()
