import math
from sys import stdin

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    n = int(stdin.readline().strip())
    array = list(map(int, stdin.readline().strip().split()))

    # Step 4 and 5: Check if the GCD of the entire array is 1
    overall_gcd = array[0]
    for num in array:
        overall_gcd = gcd(overall_gcd, num)

    if overall_gcd != 1:
        print(-1)
        return

    # Step 7 and 8: Find the minimum number of operations required
    min_operations = 0
    for i in range(n):
        current_gcd = array[i]
        operations = 0
        for j in range(i, n):
            current_gcd = gcd(current_gcd, array[j])
            operations += 1
            if current_gcd == 1:
                min_operations = max(min_operations, operations)
                break

    print(min_operations - 1)  # Subtract 1 because we counted the first element twice

if __name__ == "__main__":
    main()
