import sys

def solution():
    n = int(input())
    s = input()

    # Initialize maximum possible value to 0
    max_value = 0

    # Iterate over all possible pairs of substrings
    for i in range(n):
        for j in range(i + 1, n):
            # Extract the current pair of substrings
            substring1 = s[i:j+1]
            substring2 = s[j:]

            # Calculate bitwise OR operation for this pair
            or_value = int(substring1, 2) | int(substring2, 2)

            # Update maximum possible value if necessary
            max_value = max(max_value, or_value)

    print(bin(max_value)[2:].zfill(n).lstrip('0') or '0')

solution()
