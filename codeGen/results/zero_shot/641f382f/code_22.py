import math
from sys import stdin

def main():
    n = int(stdin.readline().strip())
    array = list(map(int, stdin.readline().strip().split()))

    # If there is only one element and it's not 1, it's impossible to make all elements 1
    if n == 1 and array[0] != 1:
        print(-1)
        return

    # Check if there is a pair with GCD 1
    for i in range(n - 1):
        if math.gcd(array[i], array[i + 1]) == 1:
            print(n)  # If GCD is 1, we can make the whole array 1 in n operations
            return
    
    print(-1)  # If no such pair exists, it's impossible to make all elements 1

if __name__ == "__main__":
    main()
