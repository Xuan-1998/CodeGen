import math
from sys import stdin

def main():
    # Read the input
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))

    # Check if there's already a 1 in the array
    if 1 in arr:
        print(n - arr.count(1))  # The number of operations is n minus the number of 1's
        return
    
    # Check if it's possible to create a 1 by combining elements
    for i in range(n-1):
        if math.gcd(arr[i], arr[i+1]) == 1:
            print(n - 1)  # We can combine this pair to eventually make all elements 1
            return
    
    # If it's not possible, return -1
    print(-1)

if __name__ == "__main__":
    main()
