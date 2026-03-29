import sys
from math import gcd

# Function to find the shortest subsequence with GCD 1
def find_shortest_subsequence_gcd_1(arr):
    n = len(arr)
    min_length = float('inf')
    for i in range(n):
        current_gcd = arr[i]
        if current_gcd == 1:
            return 1  # We found a 1, so the shortest subsequence is just this element
        for j in range(i + 1, n):
            current_gcd = gcd(current_gcd, arr[j])
            if current_gcd == 1:
                min_length = min(min_length, j - i + 1)
                break
    return min_length if min_length != float('inf') else -1

# Function to calculate the minimum number of operations
def min_operations_to_make_ones(arr):
    overall_gcd = arr[0]
    for num in arr[1:]:
        overall_gcd = gcd(overall_gcd, num)
        if overall_gcd == 1:
            break
    if overall_gcd > 1:
        return -1  # Not possible to make all elements equal to 1
    return find_shortest_subsequence_gcd_1(arr) - 1  # Subtract 1 because the first operation gives us a 1

# Read input from stdin
def main():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    print(min_operations_to_make_ones(arr))

if __name__ == "__main__":
    main()
